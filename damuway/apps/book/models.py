from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='book_covers/')
    description = models.TextField()
    genre = models.ManyToManyField(Genre)
    quote = models.TextField(blank=True, null=True)
    release_date = models.DateField()
    page_count = models.IntegerField()
    age_limit = models.CharField(max_length=10, blank=True)
    pdf_file = models.FileField(upload_to='pdfs/', blank=True, null=True)
    audio_file = models.FileField(upload_to='audios/', blank=True, null=True)
    is_new = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    is_recommended = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Quote(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='quotes')
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

class Review(models.Model):
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.book} - {self.rating}'

