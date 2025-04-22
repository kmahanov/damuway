from django.db import models
from django.contrib.auth import get_user_model


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


class ArticleLike(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        unique_together = ('article', 'user')


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
