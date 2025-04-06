from django.db import models

class AboutUs(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    mission = models.TextField(verbose_name="Миссия", blank=True, null=True)
    vision = models.TextField(verbose_name="Видение", blank=True, null=True)
    image = models.ImageField(upload_to='about/', blank=True, null=True, verbose_name="Изображение")

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    role = models.CharField(max_length=255, verbose_name="Роль")
    bio = models.TextField(verbose_name="Описание", blank=True, null=True)
    photo = models.ImageField(upload_to='team/', blank=True, null=True, verbose_name="Фото")

    def __str__(self):
        return f"{self.name} - {self.role}"
