from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=120, blank=False)
    last_name = models.CharField(max_length=120, blank=False)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=100, blank=False)
    last_login = models.DateTimeField(_('last login'), blank=True, null=True)
    is_active = models.BooleanField(default=False,db_column='is_active')

    def __unicode__(self):
        return self.first_name+self.last_name

    def get_full_username(self):
        return self.first_name + ' '+ self.last_name

    def is_authenticated(self):
        return True