from django.contrib.auth import get_user_model
from django.db import models

class ChildDevelopment(models.Model):
    AGE_CHOICES = [(i, f"{i} месяцев") for i in range(1, 73)]

    age = models.IntegerField(choices=AGE_CHOICES, unique=True, verbose_name="Возраст (месяцев)")
    physical = models.TextField(verbose_name="Физическое развитие")
    speech = models.TextField(verbose_name="Речевое развитие")
    emotional = models.TextField(verbose_name="Эмоциональное развитие")
    social = models.TextField(verbose_name="Социальное развитие")
    recommendations = models.TextField(verbose_name="Рекомендации родителям")

    image = models.URLField(blank=True, null=True, verbose_name="Изображение (ссылка)")
    source = models.URLField(blank=True, null=True, verbose_name="Источник информации")

    class Meta:
        verbose_name = "Этап развития"
        verbose_name_plural = "Развитие ребенка по возрасту"
        ordering = ["age"]

    def __str__(self):
        return f"Развитие ребенка в {self.age} месяцев"

class DevelopmentComment(models.Model):
    development = models.ForeignKey(ChildDevelopment, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="Development_comments")
    text = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"Комментарий от {self.user.username} ({self.development.age} мес.)"
