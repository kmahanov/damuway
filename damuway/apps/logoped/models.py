from django.db import models
from django.conf import settings


class Logoped(models.Model):
    SPECIALIZATIONS = [
        ("Дислалия", "Дислалия"),
        ("Дизартрия", "Дизартрия"),
        ("Заикание", "Заикание"),
        ("Афазия", "Афазия"),
        ("Общий", "Общий логопед"),
    ]

    name = models.CharField(max_length=100, verbose_name="Имя")
    specialization = models.CharField(
        max_length=50, choices=SPECIALIZATIONS, verbose_name="Специализация"
    )
    experience = models.PositiveIntegerField(verbose_name="Опыт (лет)")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True, null=True)
    email = models.EmailField(verbose_name="Email", blank=True, null=True)
    photo = models.ImageField(upload_to="logopeds/", verbose_name="Фото", blank=True, null=True)
    price_per_hour = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name="Цена за час (₸)"
    )
    location = models.CharField(max_length=255, verbose_name="Местоположение", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return f"{self.name} ({self.specialization})"

class Schedule(models.Model):
    logoped = models.ForeignKey(Logoped, on_delete=models.CASCADE, related_name="schedules")
    day_of_week = models.CharField(max_length=20, verbose_name="День недели")
    time_slot = models.CharField(max_length=20, verbose_name="Время")

    def __str__(self):
        return f"{self.logoped.name} - {self.day_of_week} {self.time_slot}"

class Review(models.Model):
    logoped = models.ForeignKey(Logoped, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="logoped_reviews")
    text = models.TextField(verbose_name="Отзыв")
    rating = models.PositiveIntegerField(verbose_name="Оценка (1-5)", default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.rating}⭐ ({self.logoped.name})"

class Appointment(models.Model):
    AGE_GROUPS = [
        ("3-5", "3-5 лет"),
        ("6-8", "6-8 лет"),
        ("9-12", "9-12 лет"),
    ]

    logoped = models.ForeignKey(Logoped, on_delete=models.CASCADE, related_name="appointments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="logoped_appointments")
    child_age_group = models.CharField(
        max_length=10, choices=AGE_GROUPS, verbose_name="Возраст ребенка"
    )
    date = models.DateField(verbose_name="Дата сеанса")
    time = models.TimeField(verbose_name="Время сеанса")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} -> {self.logoped.name} ({self.date} {self.time})"

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='booking_logoped')  # Пользователь, который записался
    logoped = models.ForeignKey('Logoped', on_delete=models.CASCADE)  # Логопед, к которому запись
    date_time = models.DateTimeField()  # Дата и время записи
    status = models.CharField(max_length=20, choices=[
        ('confirmed', 'Подтверждено'),
        ('canceled', 'Отменено'),
        ('pending', 'В ожидании'),
    ], default='pending')

    def __str__(self):
        return f"{self.user} -> {self.logoped.name} ({self.date_time})"