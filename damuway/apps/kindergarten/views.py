from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import  Kindergarten, KindergartenReview
from ..school.models import District
from .forms import KindergartenReviewForm, KindergartenSearchForm
from django.conf import settings

def district_list(request):
    districts = District.objects.all().order_by('name')
    context = {
        'districts': districts,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'kindergarten/district_list.html', context)

def kindergarten_list(request, district_id):
    district = get_object_or_404(District, id=district_id)
    kindergartens = Kindergarten.objects.filter(district=district).order_by('name')

    paginator = Paginator(kindergartens, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'district': district,
        'page_obj': page_obj,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'kindergarten/kindergarten_list.html', context)



def kindergarten_detail(request, kindergarten_id):
    kindergarten = get_object_or_404(Kindergarten, id=kindergarten_id)
    reviews = kindergarten.reviews.all().order_by('-created_at')

    review_paginator = Paginator(reviews, 5)
    review_page = request.GET.get('review_page')
    review_page_obj = review_paginator.get_page(review_page)


    form = None
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = KindergartenReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.kindergarten = kindergarten
                review.save()
                kindergarten.update_rating()
                return redirect('kindergarten:kindergarten_detail', kindergarten_id=kindergarten.id)
        else:
            form = KindergartenReviewForm()

    context = {
        'kindergarten': kindergarten,
        'review_page_obj': review_page_obj,
        'form': form,
    }
    return render(request, 'kindergarten/kindergarten_detail.html', context)


@login_required
def add_kindergarten_review(request, kindergarten_id):
    kindergarten = get_object_or_404(Kindergarten, id=kindergarten_id)

    if request.method == 'POST':
        form = KindergartenReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.kindergarten = kindergarten
            review.save()
            kindergarten.update_rating()
            return redirect('kindergarten_detail', kindergarten_id=kindergarten.id)
    else:
        form = KindergartenReviewForm()

    context = {
        'form': form,
        'kindergarten': kindergarten,
    }
    return render(request, 'kindergarten/add_review.html', context)


def search_kindergartens(request):
    form = KindergartenSearchForm(request.GET or None)
    kindergartens = Kindergarten.objects.all().order_by('name')

    if form.is_valid():
        district = form.cleaned_data.get('district')
        kindergarten_type = form.cleaned_data.get('kindergarten_type')
        min_rating = form.cleaned_data.get('min_rating')

        if district:
            kindergartens = kindergartens.filter(district=district)
        if kindergarten_type:
            kindergartens = kindergartens.filter(kindergarten_type=kindergarten_type)
        if min_rating:
            kindergartens = kindergartens.filter(rating__gte=min_rating)

    context = {
        'form': form,
        'kindergartens': kindergartens,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'kindergarten/search.html', context)
