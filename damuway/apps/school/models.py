from django.conf import settings
from django.contrib.sites import requests
from django.db import models
from math import radians, sin, cos, sqrt, atan2


class District(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='districts/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class School(models.Model):
    SCHOOL_TYPES = (
        ('state', 'Государственный'),
        ('private', 'Частный'),
        ('semi-private', 'Полу-частный'),
    )

    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    school_type = models.CharField(max_length=20, choices=SCHOOL_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=100)
    achievements = models.TextField(blank=True)
    working_hours = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    address = models.TextField()
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    rating = models.FloatField(default=0)
    main_image = models.ImageField(upload_to='schools/')

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

    def nearby_schools(self, radius_km=5):
        if not self.latitude or not self.longitude:
            return []

        lat, lng = radians(self.latitude), radians(self.longitude)
        schools = School.objects.exclude(id=self.id).exclude(latitude=None).exclude(longitude=None)

        nearby = []
        for school in schools:
            try:
                slat, slng = radians(school.latitude), radians(school.longitude)
                dlat, dlng = slat - lat, slng - lng
                a = sin(dlat / 2) ** 2 + cos(lat) * cos(slat) * sin(dlng / 2) ** 2
                c = 2 * atan2(sqrt(a), sqrt(1 - a))
                distance = 6371 * c

                if distance <= radius_km:
                    school.distance = round(distance, 2)
                    nearby.append(school)
            except:
                continue

        return sorted(nearby, key=lambda x: x.distance)

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


class SchoolImage(models.Model):
    school = models.ForeignKey(School, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='schools/gallery/')

    def __str__(self):
        return f"Изображение для {self.school.name}"


class SchoolVideo(models.Model):
    school = models.ForeignKey(School, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='schools/videos/', blank=True, null=True)
    youtube_link = models.URLField(blank=True)

    def __str__(self):
        return f"Видео для {self.school.name}"


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='school_reviews',)
    school = models.ForeignKey(School, related_name='reviews', on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв от {self.user.username} для {self.school.name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.school.update_rating()

