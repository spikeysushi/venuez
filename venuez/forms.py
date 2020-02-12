from django import forms
from .models import Profile, Venue, Booking, Venue_Img, Rating, Contact
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
        labels={
            'civilID': "Civil ID"
        }

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    # reservation = forms.DateField(widget=widgets.AdminDateWidget())
    class Meta:
        model = Booking
        fields = [ 'reservation', 'comments']
        widgets = {
            'reservation': forms.DateInput(attrs={"type":"date"})
        }

class Venue_ImgForm(forms.ModelForm):
    class Meta:
        model = Venue_Img
        fields = ['image']
        widgets ={
            'image': forms.FileInput(attrs={"class":"btn btn-success","style":"width:250px"})
        }



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

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'email' : forms.EmailInput(   attrs={
                'class':'form-control form-control-lg form-control-a',
                'name':'email',
                'type':'email',
                'placeholder':'Your Email',
                'data-rule':'email',
                'data-msg':'Please enter a valid email'
                

            }),
            'name': forms.TextInput(attrs = {
                'class':'form-control form-control-lg form-control-a',
                'placeholder':"Your Name",
                'name':'name',
                'type':'text',
                'data-rule':"minlen:4" ,
                'data-msg':"Please enter at least 4 chars"
            }),
            'subject': forms.TextInput( attrs = {
                'class':'form-control form-control-lg form-control-a',
                'name':'subject',
                'type':'text',
                'placeholder':'Subject',
                'data-rule':'minlen:4',
                'data-msg':'Please enter at least 8 chars of subject'
            }),
            'message': forms.TextInput( attrs = {
                'class':'form-control',
                'name':'message',
                'type':'text',
                'placeholder':'Message',
                'data-rule':'required',
                'data-msg':'Please write something for us'
                
            })

        }

       

       

        

     