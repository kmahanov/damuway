from django.urls import path
from .views import activity_list, activity_detail, add_rating

urlpatterns = [
    path('', activity_list, name='activity_list'),
    path('<int:pk>/', activity_detail, name='activity_detail'),
    path('<int:pk>/rate/', add_rating, name='add_rating'),
]