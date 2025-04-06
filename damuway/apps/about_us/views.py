from django.shortcuts import render
from .models import AboutUs, TeamMember

def about_us(request):
    about = AboutUs.objects.first()
    team = TeamMember.objects.all()
    return render(request, "about_us/about_us.html", {"about": about, "team": team})