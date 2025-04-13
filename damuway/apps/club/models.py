from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User

class Club(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField(blank=True)
    min_age = models.PositiveIntegerField(default=3)
    schedule = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class ClubReview(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, f'{i} ★') for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.club.name} - {self.user.username}'
