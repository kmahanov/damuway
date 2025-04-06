from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    AGE_GROUPS = [
        ('0-1', '0-1 год'),
        ('1-3', '1-3 года'),
        ('3-6', '3-6 лет'),
        ('6+', '6+ лет'),
    ]

    title = models.CharField(max_length=255, verbose_name="Название игры")
    description = models.TextField(verbose_name="Описание")
    age_group = models.CharField(max_length=3, choices=AGE_GROUPS, verbose_name="Возрастная категория")
    activity_type = models.CharField(max_length=255, verbose_name="Тип игры")
    materials = models.TextField(verbose_name="Необходимые материалы", blank=True)
    image_url = models.URLField(verbose_name="Ссылка на изображение", blank=True)
    video_url = models.URLField(verbose_name="Ссылка на видео", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    average_rating = models.FloatField(default=0.0, verbose_name="Средний рейтинг")

    def __str__(self):
        return self.title

    def update_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            self.average_rating = sum(rating.value for rating in ratings) / ratings.count()
        else:
            self.average_rating = 0.0
        self.save()

class Rating(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="ratings")
    name = models.CharField(max_length=100, verbose_name="Имя родителя")
    value = models.PositiveIntegerField(verbose_name="Оценка (1-5)", choices=[(i, i) for i in range(1, 6)])


    def __str__(self):
        return self.name


