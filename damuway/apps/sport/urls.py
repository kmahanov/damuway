from django.urls import path
from . import views

urlpatterns = [
    path('', views.sports_club_list, name='sports_club_list'),
    path('<int:pk>/', views.sports_club_detail, name='sports_club_detail'),
]