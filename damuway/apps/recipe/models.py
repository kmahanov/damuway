from django.db import models
from django.db.models import CASCADE
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


class Recipe(models.Model):
    AGE_GROUPS = [
        ('0-6', '0-6 месяцев'),
        ('6-12', '6-12 месяцев'),
        ('1-3', '1-3 года'),
        ('3-6', '3-6 лет'),
        ('6+', '6+ лет'),
    ]

    title = models.CharField(max_length=200, verbose_name=_("Название"))
    age_group = models.CharField(
        max_length=10,
        choices=AGE_GROUPS,
        verbose_name=_("Возрастная группа"),
        default='1-3',
    )
    ingredients = models.TextField(verbose_name=_("Ингредиенты"))
    instructions = models.TextField(verbose_name=_("Способ приготовления"))

    image = models.ImageField(
        upload_to='recipes/',
        blank=True,
        null=True,
        verbose_name=_("Изображение (файл)"),
    )
    image_url = models.URLField(
        blank=True,
        null=True,
        verbose_name=_("Изображение (ссылка)"),
    )

    average_rating = models.FloatField(default=0, verbose_name=_("Средний рейтинг"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return self.image_url or "/static/images/default_recipe.png"


class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=CASCADE,
        related_name="comments",
        verbose_name=_("Рецепт"),
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=CASCADE,
        related_name='comments_recipe',
    )
    text = models.TextField(verbose_name=_("Комментарий"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата добавления"))

    def __str__(self):
        return f"Комментарий от {self.user.username} к {self.recipe.title}"


class Rating(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=CASCADE,
        related_name="ratings",
        verbose_name=_("Рецепт"),
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=CASCADE,
        related_name='ratings',
    )
    value = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name=_("Оценка"),
    )

    class Meta:
        unique_together = ('user', 'recipe')

    def __str__(self):
        return f"Рейтинг {self.value} от {self.user.username} для {self.recipe.title}"