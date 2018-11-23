from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=120, blank=False)
    last_name = models.CharField(max_length=120, blank=False)
    email = models.EmailField(blank=False,unique=True)
    password = models.CharField(max_length=100, blank=False)
    last_login = models.DateTimeField(_('last login'), blank=True, null=True)
    is_active = models.BooleanField(default=False,db_column='is_active')

    def __unicode__(self):
        return self.first_name+self.last_name

    def get_full_username(self):
        return self.first_name + ' '+ self.last_name

    def is_authenticated(self):
        return True
class User_profile(models.Model):
    #first_name = models.CharField(max_length=120, blank=False)
    #last_name = models.CharField(max_length=120, blank=False)
    date_of_birth = models.DateField(max_length=8)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES)
    #email = models.EmailField(blank=False)
    permanent_address=models.CharField(max_length=300, blank=False)
    qualification=models.CharField(max_length=120, blank=False)
    occupation=models.CharField(max_length=120, blank=False)
    skills=models.CharField(max_length=200, blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    email = models.EmailField(blank=False)
    #availibility_time=models.TimeField(blank=False)
    Available_service_area=models.CharField(max_length=120, blank=False)
    '''Language_choices = (
        (u'E', u'English'),
        (u'F', u'French'),
    )'''
    languages_known= models.CharField(max_length=10, blank=False)
    Working_experience=models.CharField(max_length=120, blank=False)
    charges=models.CharField(max_length=5, blank=False)
    Profile_Tagline=models.CharField(max_length=2000, blank=False)
    user = models.ForeignKey(
        User,
        related_name='user',
        on_delete=models.CASCADE
    )


