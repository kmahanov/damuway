from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant
from .forms import RestaurantFilterForm, RestaurantReviewForm
from django.contrib.auth.decorators import login_required

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    form = RestaurantFilterForm(request.GET or None)

    if form.is_valid():
        city = form.cleaned_data.get('city')
        has_kids_menu = form.cleaned_data.get('has_kids_menu')

        if city:
            restaurants = restaurants.filter(city__icontains=city)
        if has_kids_menu == 'yes':
            restaurants = restaurants.filter(has_kids_menu=True)
        elif has_kids_menu == 'no':
            restaurants = restaurants.filter(has_kids_menu=False)

    context = {
        'restaurants': restaurants,
        'form': form
    }
    return render(request, 'restaurant/restaurant_list.html', context)


def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    return render(request, 'restaurant/restaurant_detail.html', {'restaurant': restaurant})


@login_required
def add_review(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)

    if request.method == 'POST':
        form = RestaurantReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.restaurant = restaurant
            review.save()
            return redirect('restaurant:restaurant_detail', pk=restaurant.pk)
    else:
        form = RestaurantReviewForm()

    return render(request, 'restaurant/add_review.html', {'form': form, 'restaurant': restaurant})
