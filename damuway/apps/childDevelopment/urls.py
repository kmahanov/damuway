from django.urls import path
from . import views

urlpatterns = [
    path('', views.development_list, name='development_list'),
    path('<int:age>/', views.development_detail, name='development_detail'),
]
