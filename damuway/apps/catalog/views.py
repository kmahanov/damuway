from django.shortcuts import render
from .models import Category

def web(request):
    categories = Category.objects.all()
    return render(request, "catalog/index.html", {"categories": categories})


def web(request):
    categories = [
        {"name": "Книги", "url": "/books/", "icon_name": "book.svg"},
        {"name": "Школы", "url": "/schools/", "icon_name": "school.svg"},
        {"name": "Садики", "url": "/kindergartens/", "icon_name": "kindergarten.svg"},
        {"name": "Мероприятия для семьи", "url": "/events/", "icon_name": "family-event.svg"},
        {"name": "Массаж центры", "url": "/massage/", "icon_name": "massage.svg"},
        {"name": "Логопеды", "url": "/logoped/", "icon_name": "speech-therapy.svg"},
        {"name": "Активности для детей", "url": "/activities/", "icon_name": "play.svg"},
        {"name": "Советы", "url": "/advice/", "icon_name": "advice.svg"},
        {"name": "Статья", "url": "/articles/", "icon_name": "article.svg"},
        {"name": "Развитие ребенка", "url": "/development/", "icon_name": "baby-growth.svg"},
        {"name": "Рецепты еды", "url": "/recipes/", "icon_name": "recipe.svg"},
        {"name": "Рестораны для детей", "url": "/restaurants/", "icon_name": "restaurant.svg"},
        {"name": "Спортклубы", "url": "/sport/", "icon_name": "sport.svg"},
        {"name": "Кружки для детей", "url": "/clubs/", "icon_name": "club.svg"},
        {"name": "Опросы для родителей", "url": "/surveys/", "icon_name": "survey.svg"},
    ]
    return render(request, 'catalog/index.html', {'categories': categories})
