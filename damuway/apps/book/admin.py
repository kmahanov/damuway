from django.contrib import admin

from .models import Quote, Author, Book, Genre, Review

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Quote)
admin.site.register(Genre)
admin.site.register(Review)

