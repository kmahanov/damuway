from django.contrib import admin
from .models import *
from ..school.models import School

admin.site.register(MassageCenter)
admin.site.register(MassageCategory)
admin.site.register(MassagePhoto)
admin.site.register(Review)
admin.site.register(Specialist)
admin.site.register(Appointment)

