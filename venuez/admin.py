from django.contrib import admin
from .models import Profile, Venue, Booking, Venue_Img, Rating

# Register your models here.
admin.site.register(Profile)
admin.site.register(Venue)
admin.site.register(Booking)
admin.site.register(Venue_Img)
admin.site.register(Rating)