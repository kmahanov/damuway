from django.urls import path
from . import views

urlpatterns = [
    path('', views.advice_list, name='advice_list'),
    path('advice/<int:pk>/', views.advice_detail, name='advice_detail'),
    path('advice/<int:pk>/review/', views.add_review, name='add_review'),
]