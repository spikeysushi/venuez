from django import forms
from .models import Profile, Venue, Booking, Venue_Img, Rating 
from django.contrib.auth.models import User

class RatingForm(forms.ModelForm): 
    class Meta:
        model = Rating
        fields = '__all__'

class OwnerProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','civilID']

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','paci_no']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer', 'venue', 'reservation', 'comments']
        widgets = {
            'reservation': forms.DateInput(attrs={'type':'date'}),
        }

class Venue_ImgForm(forms.ModelForm):
    class Meta:
        model = Venue_Img
        fields = ['venue', 'image']


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        exclude = ['owner']

