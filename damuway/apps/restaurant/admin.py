from django.contrib import admin

from .models import Restaurant, KidsMenuItem, RestaurantReview, RestaurantImage, MenuItemImage

admin.site.register(Restaurant)
admin.site.register(KidsMenuItem)
admin.site.register(RestaurantReview)
admin.site.register(RestaurantImage)
admin.site.register(MenuItemImage)