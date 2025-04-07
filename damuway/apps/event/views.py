from django.shortcuts import render, get_object_or_404
from .models import Event


def event_list(request):
    category = request.GET.get("category")
    search_query = request.GET.get("search")

    events = Event.objects.all().order_by("date")

    if category:
        events = events.filter(category=category)

    if search_query:
        events = events.filter(title__icontains=search_query)

    categories = Event.CATEGORY_CHOICES
    return render(request, "event/event_list.html", {"events": events, "categories": categories})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, "event/event_detail.html", {"event": event})