from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'school' 

urlpatterns = [
                  path('', views.district_list, name='district_list'),
                  path('districts/<int:district_id>/', views.school_list, name='school_list'),
                  path('schools/<int:school_id>/', views.school_detail, name='school_detail'),

                  # Отзывы
                  path('schools/<int:school_id>/review/', views.add_review, name= 'add_review'),

                  # Поиск
                  path('search/', views.search_schools, name='search_schools'),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)