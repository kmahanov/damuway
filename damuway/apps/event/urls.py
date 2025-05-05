from django.urls import path
from .views import event_list_view
from .views import EventDetailView

urlpatterns = [
    path('', event_list_view, name='event_list'),
    path('/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
]