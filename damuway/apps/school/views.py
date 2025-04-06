from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import District, School, Review
from .forms import ReviewForm, SchoolSearchForm
from django.conf import settings

def district_list(request):
    districts = District.objects.all().order_by('name')
    context = {
        'districts': districts,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'school/district_list.html', context)


def school_list(request, district_id):
    district = get_object_or_404(District, id=district_id)
    schools = School.objects.filter(district=district).order_by('name')

    # Пагинация
    paginator = Paginator(schools, 10)  # 10 школ на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'district': district,
        'page_obj': page_obj,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'school/school_list.html', context)


def school_detail(request, school_id):
    school = get_object_or_404(School, id=school_id)
    nearby_schools = school.nearby_schools(radius_km=3)  # Школы в радиусе 3 км
    reviews = school.reviews.all().order_by('-created_at')

    # Пагинация для отзывов
    review_paginator = Paginator(reviews, 5)
    review_page = request.GET.get('review_page')
    review_page_obj = review_paginator.get_page(review_page)

    context = {
        'school': school,
        'nearby_schools': nearby_schools[:5],  # Показываем только 5 ближайших
        'review_page_obj': review_page_obj,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'school/school_detail.html', context)


@login_required
def add_review(request, school_id):
    school = get_object_or_404(School, id=school_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.school = school
            review.save()
            school.update_rating()  # Обновляем рейтинг школы
            return redirect('school_detail', school_id=school.id)
    else:
        form = ReviewForm()

    context = {
        'form': form,
        'school': school,
    }
    return render(request, 'school/add_review.html', context)


def search_schools(request):
    form = SchoolSearchForm(request.GET or None)
    schools = School.objects.all().order_by('name')

    if form.is_valid():
        district = form.cleaned_data.get('district')
        school_type = form.cleaned_data.get('school_type')
        min_rating = form.cleaned_data.get('min_rating')

        if district:
            schools = schools.filter(district=district)
        if school_type:
            schools = schools.filter(school_type=school_type)
        if min_rating:
            schools = schools.filter(rating__gte=min_rating)

    context = {
        'form': form,
        'schools': schools,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'school/search.html', context)