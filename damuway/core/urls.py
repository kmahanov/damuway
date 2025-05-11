from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('apps.main.urls')),
    path('user/', include('user.urls')),
    path('book/', include('apps.book.urls')),
    path('school/', include('apps.school.urls')),
    path('massage/', include('apps.massage.urls')),
    path('logoped/', include(('apps.logoped.urls', 'logoped'), namespace='logoped')),
    path('event/', include('apps.event.urls')),
    path('about/', include('apps.about_us.urls')),
    path('activity/', include('apps.activity.urls')),
    path('advice/', include('apps.advice.urls')),
    path('article/', include('apps.article.urls')),
    path('development/', include('apps.childDevelopment.urls')),
    path('recipe/', include('apps.recipe.urls')),
    path('survey/', include('apps.survey.urls')),
    path('catalog/', include('apps.catalog.urls')),
    path('restaurant/', include('apps.restaurant.urls')),
    path('club/', include('apps.club.urls')),
    path('sport/', include('apps.sport.urls')),
    path('kindergarten/', include('apps.kindergarten.urls')),
    # path("ai/", include("ai_help.urls")),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
