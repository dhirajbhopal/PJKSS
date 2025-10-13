from django.db import models
import os
import datetime
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
#from import_export import resources


# Create your models here.


def filepathadmin(req,filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename= "%s%s" % (timeNow,old_filename)
    return os.path.join('uploads/',filename)
  


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being True")

        return self.create_user(email=email, password=password, **extra_fields)



class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True, blank=False ,null=False)
    email = models.EmailField(unique=True,null=False)
    image=models.ImageField(upload_to=filepathadmin,null=True,blank=True,default='static/images/PATEL_LOGO.png')
    mobileno=models.CharField(max_length=15,null=True,blank=True)
    gender=models.CharField(max_length=15,null=True,blank=True)
    role=models.CharField(max_length=30,null=True,blank=True)
    address=models.CharField(max_length=200,null=True,blank=True)
    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username



class letterserialno(models.Model):
    serialno=models.CharField(max_length=50,unique=True)
    issuername=models.CharField(max_length=50,blank=True,null=True)
    issuedto=models.CharField(max_length=80,blank=True,null=True)
    subject=models.CharField(max_length=30,blank=True,null=True)
    issuedate=models.DateField(blank=True, null=True)

    def __str__(self):
        return self.serialno


# date and time

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    # created automatically
    created_at = models.DateTimeField(auto_now_add=True)
    # updated whenever saved
    updated_at = models.DateTimeField(auto_now=True)

    # if you want manual datetime
    event_datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

class donation(models.Model):
    name=models.CharField(max_length=80)
    lastname=models.CharField(max_length=80)
    address=models.CharField(max_length=80)
    Amount=models.CharField(max_length=80)








