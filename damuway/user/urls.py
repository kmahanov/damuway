from django.urls import path
from . import views
from . import reset_view

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('main/', views.main, name='main'),
    path('logout/', views.logout_view, name='logout'),
    path('password_reset/', reset_view.password_reset_request, name='password_reset'),
    path('password_reset/done/', reset_view.password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', reset_view.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', reset_view.password_reset_complete, name='password_reset_complete'),
]