from django.db import models
from django.conf import settings

class MassageCategory(models.Model):

    name = models.CharField(max_length=255, unique=True, verbose_name="Категория массажа")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return self.name

class MassageCenter(models.Model):

    name = models.CharField(max_length=255, verbose_name="Название центра")
    location = models.CharField(max_length=255, verbose_name="Локация")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    rating = models.FloatField(default=0, verbose_name="Рейтинг")
    achievements = models.TextField(blank=True, null=True, verbose_name="Достижения")
    categories = models.ManyToManyField(MassageCategory, related_name="centers", verbose_name="Виды массажа")

    rating = models.FloatField(default=0, verbose_name="Рейтинг")

    def update_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            total_rating = sum([review.rating for review in reviews])
            self.rating = total_rating / reviews.count()
            self.save()

    def __str__(self):
        return self.name


    def __str__(self):
        return self.name

class MassagePhoto(models.Model):

    massage_center = models.ForeignKey(MassageCenter, related_name="photos", on_delete=models.CASCADE)
    image_url = models.URLField(verbose_name="Ссылка на фото")

    def __str__(self):
        return f"Фото {self.massage_center.name}"

class Specialist(models.Model):

    name = models.CharField(max_length=255, verbose_name="Имя специалиста")
    experience = models.PositiveIntegerField(verbose_name="Опыт работы (лет)")
    specialization = models.ForeignKey(MassageCategory, on_delete=models.CASCADE, related_name="specialists")
    massage_center = models.ForeignKey(MassageCenter, on_delete=models.CASCADE, related_name="specialists")
    photo_url = models.URLField(verbose_name="Фото специалиста", blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.specialization.name})"

class Review(models.Model):

    massage_center = models.ForeignKey(MassageCenter, related_name="reviews", on_delete=models.CASCADE)
    author = models.CharField(max_length=255, verbose_name="Имя клиента")
    rating = models.IntegerField(verbose_name="Оценка (1-5)")
    comment = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв от {self.author} - {self.rating}⭐"

class Appointment(models.Model):
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE, related_name="appointments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='massage_appointments', )
    category = models.ForeignKey(MassageCategory, on_delete=models.CASCADE, related_name="appointments")
    client_phone = models.CharField(max_length=20, verbose_name="Телефон")
    date_time = models.DateTimeField(verbose_name="Дата и время сеанса")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Запись {self.client_name} к {self.specialist.name} на {self.date_time}"
