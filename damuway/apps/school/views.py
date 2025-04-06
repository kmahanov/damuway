from django.shortcuts import render, get_object_or_404, redirect
from .models import District, School, Review
from .forms import ReviewForm, SchoolForm
from django.contrib.auth.decorators import login_required


def district_list(request):
    districts = District.objects.all()
    return render(request, 'schools/district_list.html', {'districts': districts})


def school_list(request, district_id):
    district = get_object_or_404(District, id=district_id)
    schools = School.objects.filter(district=district)
    return render(request, 'schools/school_list.html', {
        'district': district,
        'schools': schools,
        'google_maps_api_key': 'YOUR_GOOGLE_MAPS_API_KEY',
    })


def school_detail(request, school_id):
    school = get_object_or_404(School, id=school_id)
    reviews = school.reviews.all()


    if reviews.exists():
        school.rating = sum(review.rating for review in reviews) / reviews.count()
        school.save()

    return render(request, 'schools/school_detail.html', {
        'school': school,
        'reviews': reviews,
        'google_maps_api_key': 'YOUR_GOOGLE_MAPS_API_KEY',
    })


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
            return redirect('school_detail', school_id=school.id)
    else:
        form = ReviewForm()
    return render(request, 'schools/add_review.html', {'form': form, 'school': school})


@login_required
def add_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST, request.FILES)
        if form.is_valid():
            school = form.save()
            return redirect('school_detail', school_id=school.id)
    else:
        form = SchoolForm()
    return render(request, 'schools/add_school.html', {'form': form})