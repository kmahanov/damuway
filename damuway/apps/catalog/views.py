from django.shortcuts import render
from .models import Category

def web(request):
    categories = Category.objects.all()
    return render(request, "catalog/index.html", {"categories": categories})


def web(request):
    categories = [
        {"name": "Книги", "url": "/book/", "icon_name": "book.svg"},
        {"name": "Школы", "url": "/school/", "icon_name": "school.svg"},
        {"name": "Садики", "url": "/kindergarten/", "icon_name": "kindergarten.svg"},
        {"name": "Мероприятия для семьи", "url": "/event/", "icon_name": "family-event.svg"},
        {"name": "Массаж центры", "url": "/massage/", "icon_name": "massage.svg"},
        {"name": "Логопеды", "url": "/logoped/", "icon_name": "speech-therapy.svg"},
        {"name": "Активности для детей", "url": "/activity/", "icon_name": "play.svg"},
        {"name": "Советы", "url": "/advice/", "icon_name": "advice.svg"},
        {"name": "Статья", "url": "/article/", "icon_name": "article.svg"},
        {"name": "Развитие ребенка", "url": "/development/", "icon_name": "baby-growth.svg"},
        {"name": "Рецепты еды", "url": "/recipe/", "icon_name": "recipe.svg"},
        {"name": "Рестораны для детей", "url": "/restaurant/", "icon_name": "restaurant.svg"},
        {"name": "Спортклубы", "url": "/sport/", "icon_name": "sport.svg"},
        {"name": "Кружки для детей", "url": "/club/", "icon_name": "club.svg"},
        {"name": "Опросы для родителей", "url": "/survey/", "icon_name": "survey.svg"},
    ]
    return render(request, 'catalog/index.html', {'categories': categories})
