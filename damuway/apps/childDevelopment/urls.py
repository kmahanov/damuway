from django.urls import path
from . import views

urlpatterns = [
    path('', views.development_list, name='development_list'),
    path('<int:pk>/', views.development_detail, name='development_detail'),
    path('<int:pk>/comment/', views.add_comment, name='add_comment'),
]