from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from phone_field import PhoneField
# Create your models here.


class UserInfo(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), blank=True, unique=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(null=True, blank=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class Manager(models.Model):
    user = models.OneToOneField(UserInfo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Employee(models.Model):
    emp_user = models.OneToOneField(UserInfo, on_delete=models.CASCADE)
    mobile = PhoneField(help_text='Phone number', unique=True, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f"{self.emp_user.first_name} {self.emp_user.last_name}"
