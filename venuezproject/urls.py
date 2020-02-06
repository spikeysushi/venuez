"""venuezproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from venuez import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('profile/', views.shop_list, name="profile"),
    path('home/', views.home, name="home"), 
    path('venue/create/', views.venue_create, name="venue-create"),
    path('venue/list/',views.venue_list ,name='venue-list'),
    path('booking/create/', views.booking_create, name="booking-create"),
    path('venue/<int:venue_id>/detail/', views.venue_detail ,name='venue-detail'),
    path('venue/<int:venue_id>/update/', views.venue_update ,name='venue-update'),
    path('venue/<int:venue_id>/delete/', views.venue_delete ,name='venue-delete'),
    path('owner/create/', views.owner_create, name="owner-create"),
    path('owner/signup/', views.signup_owner, name="signup-owner"),
    path('signout/', views.signout, name="signout"),
    path('owner/profile/', views.profile_owner, name="owner-profile"),
    path('customer/create/', views.customer_create, name="customer-create"),
    path('customer/signup/', views.signup_customer, name="signup-customer"),
    path('booking/<int:venue_id>/create/', views.booking_create, name="booking-create"),
    path('signin/', views.signin, name="signin"),
    path('rating/create/', views.rating_create, name="rating-create"),
    path('customer/profile/', views.profile_customer, name="profile-customer"),
    path('no-access/', views.no_access, name="no-access"),
]
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)