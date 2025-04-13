from django.shortcuts import render, get_object_or_404, redirect
from .models import Club
from .forms import ClubFilterForm, ClubReviewForm

def club_list(request):
    clubs = Club.objects.all()
    form = ClubFilterForm(request.GET)

    if form.is_valid():
        city = form.cleaned_data.get('city')
        search = form.cleaned_data.get('search')

        if city:
            clubs = clubs.filter(city__icontains=city)
        if search:
            clubs = clubs.filter(name__icontains=search)

    return render(request, 'club/club_list.html', {'clubs': clubs, 'form': form})

def club_detail(request, pk):
    club = get_object_or_404(Club, pk=pk)

    if request.method == 'POST' and request.user.is_authenticated:
        form = ClubReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.club = club
            review.save()
            return redirect('club_detail', pk=club.pk)
    else:
        form = ClubReviewForm()

    return render(request, 'club/club_detail.html', {'club': club, 'form': form})
