from django.shortcuts import render
from .models import Restaurant
from .forms import RestaurantFilterForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant, RestaurantReview
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

def restaurant_list(request):
    form = RestaurantFilterForm(request.GET)
    restaurants = Restaurant.objects.all()

    if form.is_valid():
        city = form.cleaned_data.get('city')
        search = form.cleaned_data.get('search')

        if city:
            restaurants = restaurants.filter(city__icontains=city)

        if search:
            restaurants = restaurants.filter(name__icontains=search)

    context = {
        'form': form,
        'restaurants': restaurants
    }
    return render(request, 'restaurants/restaurant_list.html', context)


def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)

    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.restaurant = restaurant
            review.save()
            return redirect('restaurant_detail', pk=restaurant.pk)
    else:
        form = ReviewForm()

    return render(request, 'restaurants/restaurant_detail.html', {
        'restaurant': restaurant,
        'form': form
    })
