from django.shortcuts import render, get_object_or_404, redirect
from .models import HealthAdvice, ParentReview, AgeCategory
from .forms import ParentReviewForm
from django.contrib.auth.decorators import login_required

def advice_list(request):
    advices = HealthAdvice.objects.all().order_by('-created_at')
    return render(request, 'advice/advice_list.html', {'advices': advices})

def advice_detail(request, pk):
    advice = get_object_or_404(HealthAdvice, pk=pk)
    reviews = advice.reviews.all()
    form = ParentReviewForm()

    return render(request, 'advice/advice_detail.html', {
        'advice': advice,
        'reviews': reviews,
        'form': form
    })

@login_required
def add_review(request, pk):
    advice = get_object_or_404(HealthAdvice, pk=pk)

    if request.method == 'POST':
        form = ParentReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.advice = advice
            review.user = request.user
            review.save()
            return redirect('advice_detail', pk=advice.pk)
    else:
        form = ParentReviewForm()

    return render(request, 'advice/add_review.html', {
        'form': form,
        'advice': advice
    })