from django.db import models

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('festival', 'Фестиваль'),
        ('workshop', 'Мастер-класс'),
        ('exhibition', 'Выставка'),
        ('concert', 'Концерт'),
        ('theater', 'Театр'),
        ('sport', 'Спорт'),
        ('other', 'Другое'),
    ]

    title = models.CharField(max_length=255, verbose_name="Название события")
    description = models.TextField(verbose_name="Описание")
    location = models.CharField(max_length=255, verbose_name="Место проведения")
    date = models.DateTimeField(verbose_name="Дата и время")
    image = models.ImageField(upload_to="events/", blank=True, null=True, verbose_name="Фото события")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other', verbose_name="Категория")
    age_limit = models.CharField(max_length=10, verbose_name="Возрастное ограничение", default="0+")
    price = models.CharField(max_length=50, verbose_name="Цена", default="Бесплатно")
    ticket_link = models.URLField(blank=True, null=True, verbose_name="Ссылка на билеты")
    organizer = models.CharField(max_length=255, blank=True, null=True, verbose_name="Организатор")
    featured = models.BooleanField(default=False, verbose_name="Показывать в слайдере")

    def __str__(self):
        return self.title