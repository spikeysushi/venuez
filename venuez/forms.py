from django import forms
from .models import Profile, Venue, Booking, Venue_Img, Rating 
from django.contrib.auth.models import User
from django.contrib.admin import widgets

class RatingForm(forms.ModelForm): 
    star = forms.TextInput( attrs = {
     'class':'form-control-range',
     'style':'color: red',
     'id':'formControlRange',
     'type':'range'
    })
    class Meta:
        model = Rating
        fields = ['star', 'comment']
        labels = {
            'star': 'Stars',
            'comment': "What do you think of your experience?"
        }

# class RatingForm(forms.Form):
#     start = forms.CharField(widget=forms.TextInput( attrs = {
#      'class':'form-control-range',
#      'id':'formControlRange',
#      'type':'range',
#       'min':"1" ,
#       'max':"5",
#       'step':"1"

#     }))
#     comment = forms.CharField(widget=forms.TextInput())

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