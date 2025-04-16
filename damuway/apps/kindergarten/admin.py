from django.contrib import admin
from .models import Kindergarten, KindergartenImage,KindergartenReview,KindergartenVideo

admin.site.register(Kindergarten)
admin.site.register(KindergartenImage)
admin.site.register(KindergartenReview)
admin.site.register(KindergartenVideo)

