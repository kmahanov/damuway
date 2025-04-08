from django.urls import path
from .views import SurveyView, CompleteView

app_name = 'survey'

urlpatterns = [
    path('', SurveyView.as_view(), name='start'),
    path('<int:question_id>/', SurveyView.as_view(), name='question'),
    path('complete/', CompleteView.as_view(), name='complete'),
]