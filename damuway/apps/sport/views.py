from django.shortcuts import render, get_object_or_404, redirect
from .models import SportsClub
from .forms import SportsClubFilterForm, SportsClubReviewForm

def sports_club_list(request):
    clubs = SportsClub.objects.all()
    form = SportsClubFilterForm(request.GET)

    if form.is_valid():
        city = form.cleaned_data.get('city')
        sport_type = form.cleaned_data.get('sport_type')

        if city:
            clubs = clubs.filter(city__icontains=city)
        if sport_type:
            clubs = clubs.filter(sport_type=sport_type)

    return render(request, 'sports/sports_club_list.html', {'clubs': clubs, 'form': form})

def sports_club_detail(request, pk):
    club = get_object_or_404(SportsClub, pk=pk)

    if request.method == 'POST' and request.user.is_authenticated:
        form = SportsClubReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.club = club
            review.save()
            return redirect('sports_club_detail', pk=club.pk)
    else:
        form = SportsClubReviewForm()

    return render(request, 'sports/sports_club_detail.html', {'club': club, 'form': form})
