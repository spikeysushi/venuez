from django.shortcuts import render, redirect
from .models import Profile, Venue, Booking, Venue_Img, Rating 
from .forms import OwnerProfileForm, CustomerProfileForm, VenueForm, BookingForm, Venue_ImgForm, RatingForm

# Create your views here.

def rating_create(request):
    form = RatingForm()
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venue')
    context = {
        "form":form,
    }
    return render(request, 'venue.html', context)

def booking_create(request, venue_id):
    venue_obj = Venue.objects.get(id=venue_id)
    form = BookingForm()
    if  request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.venue = venue
            booking.save()
            return redirect('venue-detail', venue_id)
        context = {
            "form":form,
            "venue": venue
        }
        return render(request, 'booking.html', context)

def venue_img_create(request, venue_id):
    venue_obj = Venue.objects.get(id=venue_id)
    form = Venue_ImgForm()
    if request.method == "POST":
        form = Venue_ImgForm(request.POST)
        if form.is_valid():
            venue_img = form.save(commit=False)
            venue_img.venue = venue
            venue_img.save()
            return redirect('venue-detail', venue_id)
    context = {
        "form":form,
        "venue": venue
    }
    return render(request, 'venue_img.html', context)

def venue_list(request):
    context = {
        "venues":Venue.objects.all()
    }
    
    return render(request, 'list.html', context)

def venue_create(request):
    form = VenueForm()
    if request.method == "POST":
        form = VenueForm(request.POST, request.FILES)
        if form.is_valid():
            venue = form.save(commit=False)
            venue.owner = request.user
            venue.save()
            return redirect('venue-list')
    context = {
        "form":form,
    }
    return render(request, 'venue-create.html', context)

def venue_detail(request, venue_id):
    venue=Venue.objects.get(id=venue_id)
    context = {
        "venue":venue ,
    }
    return render(request, 'venue-detail.html', context)

def venue_update(request, venue_id):
    venue_obj = Venue.objects.get(id=venue_id)
    form = VenueForm(instance=venue_obj)
    if request.method == "POST":
        form = VenueForm(request.POST, request.FILES, instance=venue_obj)
        if form.is_valid():
            form.save()
            return redirect('venue-list')
    context = {
        "venue_obj": venue_obj,
        "form":form,
    }
    return render(request, 'update.html', context)

def venue_delete(request, venue_id):
    venue_obj = venue.objects.get(id=venue_id)
    venue_obj.delete()
    return redirect('venue-list')

def booking_delete(request, booking_id):
    booking_obj = booking.objects.get(id=booking_id)
    booking_obj.delete()
    return redirect('booking-list')

def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect("restaurant-list")
    context = {
        "form":form,
    }
    return render(request, 'signup.html', context)

def signin(request):
    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('home.html')
    context = {
        "form":form
    }
    return render(request, 'signin.html', context)

def signout(request):
    logout(request)
    return redirect("signin")
    