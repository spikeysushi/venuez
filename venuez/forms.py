from django import forms
from .models import Profile, Venue, Booking, Venue_Img, Rating 
from django.contrib.auth.models import User
from django.contrib.admin import widgets
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

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    reservation = forms.DateField(widget=widgets.AdminDateWidget())
    class Meta:
        model = Booking
        fields = [ 'venue', 'reservation', 'comments']
        # widgets = {
        #     'reservation': forms.DateInput(attrs = {
        #         'class': 'datepicker'
        #     })
        # }

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

class SigninForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())