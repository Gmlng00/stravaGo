from django.contrib import admin
from reservationApp.models import Category, Location, Run, Schedule, Booking
# Register your models here.
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Run)
admin.site.register(Schedule)
admin.site.register(Booking)
