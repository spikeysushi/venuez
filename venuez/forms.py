from django import forms
from .models import Profile, Venue, Booking, Venue_Img, Rating 
from django.contrib.auth.models import User

class RatingForm(forms.ModelForm): 
    class Meta:
        model = Rating
        exclude = ['customer', 'booking','venue']

class OwnerProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','civilID', 'user_type']

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','paci_no','user_type']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [ 'venue', 'reservation', 'comments']
        widgets = {
            'reservation': forms.DateInput(attrs={'type':'date'}),
        }

class Venue_ImgForm(forms.ModelForm):
    class Meta:
        model = Venue_Img
        fields = ['image']


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        exclude = ['owner']

class UserRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' ,'password']

        widgets={
        'password': forms.PasswordInput(),
        }
