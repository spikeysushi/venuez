from django.shortcuts import render, redirect
from .models import Profile, Venue, Booking, Venue_Img, Rating, Contact
from .forms import OwnerProfileForm, CustomerProfileForm, VenueForm, BookingForm, Venue_ImgForm, RatingForm, UserRegister, SigninForm, ContactForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def which_profile(request):
    profile = Profile.objects.get(user= request.user)
    if profile.user_type == "OWNER":
        return redirect('owner-profile')
    else:
        return redirect('profile-customer')

def rating_create(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    profile = Profile.objects.get(user=request.user)
    form = RatingForm()
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.venue = venue
            rating.customer = profile
            rating.save()
            return redirect('venue-list')
    context = {
        "form":form,
        "venue":venue
    }
    return render(request, 'rating_create.html', context)

def booking_create(request, venue_id):
    if not request.user.is_authenticated :
        return redirect('signin')
    venue = Venue.objects.get(id=venue_id)
    profile = Profile.objects.get(user= request.user)
    form = BookingForm()
    if  request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.venue = venue
            booking.customer = profile
            booking.save()
            return redirect('venue-detail', venue_id)
    context = {
        "form":form,
        "venue":venue
    }
    return render(request, 'booking_create.html', context)

def booking_update(request, booking_id):
    if not request.user.is_authenticated :
        return redirect('signin')
    booking = Booking.objects.get(id=booking_id)
    form = BookingForm(instance=booking)
    if  request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('profile')
    context = {
        "form":form,
        "booking":booking
    }
    return render(request, 'booking_update.html', context)

def venue_img_create(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    images = Venue_Img.objects.filter(venue=venue)
    form = Venue_ImgForm()
    if request.method == "POST":
        form = Venue_ImgForm(request.POST, request.FILES)
        if form.is_valid():
            venue_img = form.save(commit=False)
            venue_img.venue = venue
            venue_img.save()
            return redirect('venue-detail', venue_id)
    context = {
        "form":form,
        "venue": venue,
        "images":images
    }
    return render(request, 'venue_img_create.html', context)

def venue_list(request):
    context = {
        "venues":Venue.objects.all()
    }
    
    return render(request, 'venue_list.html', context)

def venue_create(request):
    profile = Profile.objects.get(user=request.user)
    if profile.user_type == "Customer":
        return redirect('no-access')
    form = VenueForm()
    if request.method == "POST":
        form = VenueForm(request.POST, request.FILES)
        if form.is_valid():
            venue = form.save(commit=False)
            venue.owner=profile
            venue.save()
            return redirect('venue-img', venue.id)
    context = {
        "form":form,
    }
    return render(request, 'venue_create.html', context)

def no_access(request):
    return render(request,'no_access.html')

def venue_detail(request, venue_id):
    venue=Venue.objects.get(id=venue_id)
    venue_images = Venue_Img.objects.filter(venue=venue)
    context = {
        "venue":venue ,
        "images":venue_images
    }
    return render(request, 'venue_detail.html', context)

def venue_update(request, venue_id):
    venue_obj = Venue.objects.get(id=venue_id)
    form = VenueForm(instance=venue_obj)
    if request.method == "POST":
        form = VenueForm(request.POST, request.FILES, instance=venue_obj)
        if form.is_valid():
            form.save()
            return redirect('venue-detail', venue_obj.id)
    context = {
        "venue_obj": venue_obj,
        "form":form,
    }
    return render(request, 'update.html', context)

def venue_delete(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    venue.delete()
    return redirect('venue-list')

def venue_img_delete(request, image_id):
    image = Venue_Img.objects.get(id=image_id)
    venue = Venue.objects.get(id=image.venue.id)
    image.delete()
    return redirect('venue-detail', venue.id)

def booking_delete(request, booking_id):
    booking_obj = Booking.objects.get(id=booking_id)
    booking_obj.delete()
    return redirect('profile')

def signup_owner(request):
    form = UserRegister()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect("owner-create")
    context = {
        "form":form,
    }
    return render(request, 'signup_owner.html', context)

def owner_create(request):
    form = OwnerProfileForm()
    if request.method == "POST":
        form = OwnerProfileForm(request.POST, request.FILES)
        if form.is_valid():
            owner = form.save(commit=False)
            owner.user = request.user
            owner.user_type = 'OWNER'
            owner.save()
            return redirect('home')
    context = {
        "form":form,
    }
    return render(request, 'owner_create.html', context)

def signup_customer(request):
    form = UserRegister()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect("customer-create")
    context = {
        "form":form,
    }
    return render(request, 'signup_customer.html', context)

def customer_create(request):
    form = CustomerProfileForm()
    if request.method == "POST":
        form = CustomerProfileForm(request.POST, request.FILES)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.user_type = 'CUSTOMER'
            customer.save()
            return redirect('home')
    context = {
        "form":form,
    }
    return render(request, 'customer_create.html', context)

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
                return redirect('home')
    context = {
        "form":form
    }
    return render(request, 'signin.html', context)

def signout(request):
    logout(request)
    return redirect("home")

def home(request):
    context = {
        "images":Venue_Img.objects.all()[3:],
        "ratings": Rating.objects.all()[:3]
    }
    return render(request, "home.html",context)

def profile_owner(request):
    profile=Profile.objects.get(user=request.user)
    venues = Venue.objects.filter(owner=profile)
    context = {
        "profile" : profile,
        "venues":venues
    }
    return render(request, 'owner_profile.html', context)

def profile_customer(request):
    context = {
        "profile":Profile.objects.get(user=request.user)
    }
    return render(request, 'customer_profile.html', context)


def about(request):
    context = {
        "images":Venue_Img.objects.all(),
        "ratings": Rating.objects.all()[:3]
    }
    return render(request, "about.html",context)

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context={
                "flag":True
            }
            return render(request, 'contact.html', context)
    context = {
        "flag": False,
        "form":form,
    }
    return render(request, 'contact.html', context)

# def venue_img_create(request, venue_id):
#     venue = Venue.objects.get(id=venue_id)
#     form = Venue_ImgForm()
#     if request.method == "POST":
#         form = Venue_ImgForm(request.POST,request.FILES)
#         if form.is_valid():
#             img = form.save(commit=False)
#             img.venue = venue
#             img.save()
#             #Make sure the url name is venue-detail
#             return redirect('venue-detail', venue_id)
#     context = {
#         "from": form,
#         "venue":venue
#     }
#     return render(request, venue_img_create.html,context)
