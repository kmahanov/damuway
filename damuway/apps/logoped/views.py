from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Logoped, Review, Appointment, Booking, Schedule
from .forms import LogopedForm, ReviewForm, AppointmentForm, BookingForm


def logoped_list(request):
    logopeds = Logoped.objects.all()
    specialization = request.GET.get('specialization')

    if specialization:
        logopeds = logopeds.filter(specialization=specialization)

    return render(request, 'logoped/list.html', {'logopeds': logopeds})


def logoped_detail(request, pk):
    logoped = get_object_or_404(Logoped, pk=pk)
    schedules = Schedule.objects.filter(logoped=logoped)
    reviews = Review.objects.filter(logoped=logoped)

    if request.method == 'POST' and request.user.is_authenticated:
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.logoped = logoped
            review.user = request.user
            review.save()
            messages.success(request, 'Ваш отзыв был добавлен!')
            return redirect('detail', pk=pk)
    else:
        review_form = ReviewForm()

    return render(request, 'logoped/detail.html', {
        'logoped': logoped,
        'schedules': schedules,
        'reviews': reviews,
        'review_form': review_form,
    })


@login_required
def create_appointment(request, pk):
    logoped = get_object_or_404(Logoped, pk=pk)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.logoped = logoped
            appointment.user = request.user
            appointment.save()

            # Create a booking as well
            Booking.objects.create(
                user=request.user,
                logoped=logoped,
                date_time=f"{form.cleaned_data['date']} {form.cleaned_data['time']}",
                status='confirmed'
            )

            messages.success(request, 'Вы успешно записались на прием!')
            return redirect('logoped_detail', pk=pk)
    else:
        form = AppointmentForm()

    return render(request, 'logoped/appointment.html', {
        'form': form,
        'logoped': logoped,
    })


@login_required
def create_booking(request, pk):
    logoped = get_object_or_404(Logoped, pk=pk)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.logoped = logoped
            booking.save()
            messages.success(request, 'Запись успешно создана!')
            return redirect('profile')
    else:
        form = BookingForm()

    return render(request, 'logoped/booking.html', {
        'form': form,
        'logoped': logoped,
    })


@login_required
def user_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-date_time')
    return render(request, 'logoped/user_bookings.html', {'bookings': bookings})


@login_required
def user_reviews(request):
    reviews = Review.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'logoped/user_reviews.html', {'reviews': reviews})


@login_required
def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)

    if request.method == 'POST':
        booking.status = 'canceled'
        booking.save()
        messages.success(request, 'Запись была отменена.')
        return redirect('user_bookings')

    return render(request, 'logoped/cancel_booking.html', {'booking': booking})