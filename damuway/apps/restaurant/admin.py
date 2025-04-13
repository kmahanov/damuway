from django.contrib import admin

from .models import Restaurant, KidsMenuItem, RestaurantReview

admin.site.register(Restaurant)
admin.site.register(KidsMenuItem)
admin.site.register(RestaurantReview)
