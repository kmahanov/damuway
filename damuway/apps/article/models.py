from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Категория")

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    author = models.CharField(max_length=100, verbose_name='Автор')
    content = models.TextField(verbose_name="Содержание")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="articles", verbose_name="Категория")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    image = models.ImageField(upload_to="articles/", blank=True, null=True, verbose_name="Изображение")

    def __str__(self):
        return self.title
