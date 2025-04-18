from django.urls import path
from . import views

app_name = 'sport'

urlpatterns = [
    path('', views.sports_club_list, name='club_list'),
    path('<int:pk>/', views.sports_club_detail, name='club_detail'),
    path('<int:pk>/review/', views.add_review, name='add_review'),
]