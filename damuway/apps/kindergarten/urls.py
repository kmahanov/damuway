from django.urls import path
from . import views

urlpatterns = [
    path('', views.district_list, name='kindergarten_district_list'),
    path('districts/<int:district_id>/', views.kindergarten_list, name='kindergarten_list'),
    path('kindergarten/<int:kindergarten_id>/', views.kindergarten_detail, name='kindergarten_detail'),
    #path('kindergarten/<int:kindergarten_id>/review/', views.add_review, name='add_kindergarten_review'),
    path('search/', views.search_kindergartens, name='search_kindergartens'),
]