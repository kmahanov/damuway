from django.shortcuts import render, get_object_or_404, redirect
from .models import SportsClub
from .forms import SportsClubFilterForm, SportsClubReviewForm
from django.contrib.auth.decorators import login_required

def sports_club_list(request):
    clubs = SportsClub.objects.all()
    form = SportsClubFilterForm(request.GET or None)

    if form.is_valid():
        city = form.cleaned_data.get('city')
        sport_type = form.cleaned_data.get('sport_type')

        if city:
            clubs = clubs.filter(city__icontains=city)
        if sport_type:
            clubs = clubs.filter(sport_type=sport_type)

    context = {
        'clubs': clubs,
        'form': form
    }
    return render(request, 'sport/sports_club_list.html', context)


def sports_club_detail(request, pk):
    club = get_object_or_404(SportsClub, pk=pk)
    return render(request, 'sport/sports_club_detail.html', {'club': club})


@login_required
def add_review(request, pk):
    club = get_object_or_404(SportsClub, pk=pk)

    if request.method == 'POST':
        form = SportsClubReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.club = club
            review.save()
            return redirect('sport:club_detail', pk=club.pk)
    else:
        form = SportsClubReviewForm()

    return render(request, 'sport/add_review.html', {'form': form, 'club': club})
