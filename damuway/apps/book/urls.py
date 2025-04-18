from django.urls import path
from . import views
from django.conf.urls.static import settings
from django.conf.urls.static import static

app_name = 'book'

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('<int:pk>/quotes/', views.quote_list, name='quote_list'),
    path('<int:pk>/review/', views.add_review, name='add_review'),
]
