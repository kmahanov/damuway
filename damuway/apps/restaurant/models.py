from django.contrib.auth import get_user_model
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField(blank=True, null=True)
    has_kids_menu = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class KidsMenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='kids_menu')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.restaurant.name})"


class RestaurantReview(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.restaurant.name} – {self.rating}★ by {self.user.username}"

class RestaurantImage(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='restaurant_images/')

    def __str__(self):
        return f"Фото ресторана {self.restaurant.name}"


class MenuItemImage(models.Model):
    item = models.ForeignKey(KidsMenuItem, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='menu_item_images/')

    def __str__(self):
        return f"Фото блюда {self.item.name}"