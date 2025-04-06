from django.urls import path
from . import views

app_name = 'logoped'

urlpatterns = [
    path('', views.logoped_list, name='list'),
    path('<int:pk>/', views.logoped_detail, name='detail'),
    path('<int:pk>/appointment/', views.create_appointment, name='create_appointment'),
    path('<int:pk>/booking/', views.create_booking, name='create_booking'),

    # User related URLs
    path('my-bookings/', views.user_bookings, name='user_bookings'),
    path('my-reviews/', views.user_reviews, name='user_reviews'),
    path('cancel-booking/<int:pk>/', views.cancel_booking, name='cancel_booking'),
]