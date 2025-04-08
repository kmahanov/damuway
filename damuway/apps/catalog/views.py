from django.shortcuts import render
from .models import Category

def web(request):
    categories = Category.objects.all()
    return render(request, "catagol/index.html", {"categories": categories})