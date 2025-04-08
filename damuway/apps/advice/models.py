from django.contrib.auth import get_user_model
from django.db import models

class AgeCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name

class HealthAdvice(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    age_category = models.ForeignKey(AgeCategory, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class ParentReview(models.Model):
    advice = models.ForeignKey(HealthAdvice, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="advice_reviews")
    rating = models.PositiveIntegerField(
        choices=[(i, i) for i in range(1, 6)],
        verbose_name="Оценка (1-5)"
    )
    comment = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Отзыв от {self.user.username} - {self.rating}★"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Отзыв родителя'
        verbose_name_plural = 'Отзывы родителей'