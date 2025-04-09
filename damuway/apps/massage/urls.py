from django.urls import path
from . import views
app_name = 'massage' 
urlpatterns = [
    path('centers/', views.massage_center_list, name='massage_center_list'),
    path('centers/<int:center_id>/', views.massage_center_detail, name='massage_center_detail'),
    path('centers/<int:center_id>/review/', views.add_review, name='add_review'),
    path('specialists/', views.specialist_list, name='specialist_list'),
    path('specialists/<int:specialist_id>/', views.specialist_detail, name='specialist_detail'),
    path('specialists/<int:specialist_id>/book/', views.book_appointment, name='book_appointment'),
]