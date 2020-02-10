from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Profile(models.Model):
    USER_TYPES = [
        ('NONE', 'None'),
        ('OWNER', 'Owner'),
        ('CUSTOMER', 'Customer')
    ]
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=8, choices=USER_TYPES, default='NONE' )
    paci_no = models.CharField(max_length=12, blank=True,null=True)
    civilID = models.CharField(max_length=12, blank=True, null=True)
    profile_picture = models.ImageField(null=True, blank=True)
    # You have to setup the media folder in settings 
    def __str__(self):
        return ("Profile ID:%d For:%s"%(self.id, self.user.username))

class Venue(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    location = models.CharField(max_length=130)
    name = models.CharField(max_length=100)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=3)
    description = models.TextField()
    capacity = models.IntegerField()
    availability = models.BooleanField()
    def __str__(self):
        return ("Venue ID:%d Owned By:%s"%(self.id, self.owner.user.username))

class Booking(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    reservation = models.DateField()
    comments = models.TextField()
    def __str__(self):
        return ("%d: %s"%(self.id, self.customer))

class Venue_Img(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    image = models.ImageField()
    def __str__(self):
        return "Venue Image ID:%d For Venue ID:%d Named: %s " %(self.id,self.venue.id,self.venue.name)


class Rating(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    star =  models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return ("%d: %s"%(self.id, self.customer))

    





    
