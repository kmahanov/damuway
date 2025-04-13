from django.urls import path
from . import views

urlpatterns = [
    path('', views.club_list, name='club_list'),
    path('<int:pk>/', views.club_detail, name='club_detail'),
]
