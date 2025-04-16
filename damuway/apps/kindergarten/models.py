from django.contrib.auth import get_user_model
from django.contrib.sites import requests
from django.db import models
from ..school.models import District
from django.conf import settings


class Kindergarten(models.Model):
    KINDERGARTEN_TYPES = (
        ('state', 'Государственный'),
        ('private', 'Частный'),
    )

    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    kindergarten_type = models.CharField(max_length=20, choices=KINDERGARTEN_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    age_range = models.CharField(max_length=100)
    activities = models.TextField(blank=True)
    working_hours = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    address = models.TextField()
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    rating = models.FloatField(default=0)
    main_image = models.ImageField(upload_to='kindergartens/')

    def __str__(self):
        return self.name

    def geocode_address(self):
        if not self.address or (self.latitude and self.longitude):
            return

        try:
            url = f"https://maps.googleapis.com/maps/api/geocode/json?address={self.address}&key={settings.GOOGLE_MAPS_API_KEY}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if data['results']:
                    location = data['results'][0]['geometry']['location']
                    self.latitude = location['lat']
                    self.longitude = location['lng']
                    self.save()
        except Exception as e:
            print(f"Ошибка геокодирования: {e}")

    def save(self, *args, **kwargs):
        if not self.latitude or not self.longitude:
            self.geocode_address()
        super().save(*args, **kwargs)

    def update_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            self.rating = sum(review.rating for review in reviews) / reviews.count()
        else:
            self.rating = 0
        self.save(update_fields=['rating'])

class KindergartenImage(models.Model):
    kindergarten = models.ForeignKey(Kindergarten, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='kindergartens/gallery/')

    def __str__(self):
        return f"Изображение для {self.kindergarten.name}"

class KindergartenVideo(models.Model):
    kindergarten = models.ForeignKey(Kindergarten, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='kindergartens/videos/', blank=True, null=True)
    youtube_link = models.URLField(blank=True)

    def __str__(self):
        return f"Видео для {self.kindergarten.name}"

class KindergartenReview(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='kindergarten_reviews')
    kindergarten = models.ForeignKey(Kindergarten, related_name='reviews', on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв от {self.user.username} для {self.kindergarten.name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.kindergarten.update_rating()