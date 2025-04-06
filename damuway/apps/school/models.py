from django.db import models
from django.contrib.auth.models import User


class District(models.Model):
    name = models.CharField(max_length=100)

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


class SchoolImage(models.Model):
    school = models.ForeignKey(School, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='schools/gallery/')


class SchoolVideo(models.Model):
    school = models.ForeignKey(School, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='schools/videos/', blank=True, null=True)
    youtube_link = models.URLField(blank=True)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, related_name='reviews', on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.school.name}"