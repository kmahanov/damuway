from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Activity, Rating
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

# Список всех активностей
def activity_list(request):
    activities = Activity.objects.all().order_by('-created_at')
    return render(request, 'activity/activity_list.html', {'activities': activities})

# Детальная страница активности
def activity_detail(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    return render(request, 'activity/activity_detail.html', {
        'activity': activity,
    })

# Добавление оценки (рейтинг)
@login_required
def add_rating(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == 'POST':
        value = int(request.POST.get('value'))
        rating, created = Rating.objects.update_or_create(
            user=request.user,
            activity=activity,
            defaults={'value': value}
        )
        activity.update_rating()
        messages.success(request, 'Спасибо за вашу оценку!')
    return redirect('activity_detail', pk=pk)


