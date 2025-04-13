from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User

SPORT_TYPES = [
    ('boxing', 'Бокс'),
    ('judo', 'Дзюдо'),
    ('karate', 'Каратэ'),
    ('swimming', 'Плавание'),
    ('football', 'Футбол'),
    ('gymnastics', 'Гимнастика'),
    ('taekwondo', 'Тхэквондо'),
    ('basketball', 'Баскетбол'),
    ('wrestling', 'Борьба'),
]

class SportsClub(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    address = models.TextField()
    sport_type = models.CharField(max_length=50, choices=SPORT_TYPES)
    min_age = models.PositiveIntegerField(default=5)
    schedule = models.CharField(max_length=255, blank=True)
    price = models.PositiveIntegerField(default=0, help_text="Цена за месяц в тенге")
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.get_sport_type_display()})"

class SportsClubReview(models.Model):
    club = models.ForeignKey(SportsClub, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='sports')
    rating = models.IntegerField(choices=[(i, f'{i} ★') for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.club.name} - {self.user.username}'

