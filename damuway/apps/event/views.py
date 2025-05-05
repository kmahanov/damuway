from django.shortcuts import render
from django.db.models import Q
from datetime import datetime,  date
from .models import Event
from .forms import EventFilterForm
from django.views.generic import DetailView


def event_list_view(request):
    events = Event.objects.all().order_by('date')
    featured_events = Event.objects.filter(featured=True).order_by('date')

    form = EventFilterForm(request.GET)

    if form.is_valid():
        category = form.cleaned_data.get('category')
        search = form.cleaned_data.get('search')
        selected_date = form.cleaned_data.get('date')

        if category:
            events = events.filter(category=category)
        if search:
            events = events.filter(Q(title__icontains=search) | Q(description__icontains=search))
        if selected_date:
            start = datetime.combine(selected_date, datetime.min.time())
            end = datetime.combine(selected_date, datetime.max.time())
            events = events.filter(date__range=(start, end))

    # 📆 Календарь с 1 по 31 мая
    calendar_days = range(1, 32)
    today = date.today()

    return render(request, 'event/event_list.html', {
        'form': form,
        'events': events,
        'featured_events': featured_events,
        'calendar_days': calendar_days,
        'today': today
    })

class EventDetailView(DetailView):
    model = Event
    template_name = 'event/event_detail.html'
    context_object_name = 'event'