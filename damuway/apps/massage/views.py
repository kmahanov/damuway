from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import MassageCenter, Specialist, Review, Appointment, MassageCategory
from .forms import ReviewForm, AppointmentForm


def massage_center_list(request):
    centers = MassageCenter.objects.all()
    categories = MassageCategory.objects.all()
    context = {
        'centers': centers,
        'categories': categories,
    }
    return render(request, 'massage/massage_center_list.html', context)

def massage_center_detail(request, center_id):
    center = get_object_or_404(MassageCenter, id=center_id)
    reviews = center.reviews.all().order_by('-created_at')
    specialists = center.specialists.all()

    # Пагинация для отзывов
    review_paginator = Paginator(reviews, 5)
    review_page = request.GET.get('review_page')
    review_page_obj = review_paginator.get_page(review_page)

    context = {
        'center': center,
        'reviews': reviews,
        'specialists': specialists,
        'review_page_obj': review_page_obj,
    }
    return render(request, 'massage/massage_center_detail.html', context)

# Отзывы
def add_review(request, center_id):
    center = get_object_or_404(MassageCenter, id=center_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.massage_center = center
            review.save()
            return redirect('massage_center_detail', center_id=center.id)
    else:
        form = ReviewForm()

    context = {
        'form': form,
        'center': center,
    }
    return render(request, 'massage/add_review.html', context)

# Специалисты
def specialist_list(request):
    specialists = Specialist.objects.all()
    context = {
        'specialists': specialists,
    }
    return render(request, 'massage/specialist_list.html', context)

def specialist_detail(request, specialist_id):
    specialist = get_object_or_404(Specialist, id=specialist_id)
    context = {
        'specialist': specialist,
    }
    return render(request, 'massage/specialist_detail.html', context)

# Запись на сеанс
def book_appointment(request, specialist_id):
    specialist = get_object_or_404(Specialist, id=specialist_id)
    form = AppointmentForm(request.POST or None)

    if form.is_valid():
        appointment = form.save(commit=False)
        appointment.specialist = specialist
        appointment.save()
        return redirect('massage_center_detail', center_id=specialist.massage_center.id)

    context = {
        'specialist': specialist,
        'form': form,
    }
    return render(request, 'massage/book_appointment.html', context)

