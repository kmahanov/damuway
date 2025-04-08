from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    image_url = models.URLField(blank=True, null=True)
    url = models.CharField(max_length=100, verbose_name="URL раздела", help_text="Например: 'schools' для /schools/")

    def __str__(self):
        return self.name
