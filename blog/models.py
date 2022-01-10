from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomManager

MALE = 'M'
FEMALE = 'F'
GENDER_CHOICE = (
    (MALE, 'Male'),
    (FEMALE,'female'),
)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=100)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, blank=True)
    contact = models.CharField(max_length=12)
    dob = models.DateField(default=None, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomManager()

    def __str__(self):
        return self.email


class Category(models.Model):
    Blog_categories = models.CharField(max_length=100)


class Blog(models.Model):
    Author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Blog_title = models.CharField(max_length=1000)
    Blog_category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.BooleanField(max_length=1, default=False)
    image = models.ImageField(upload_to='blog')
    Description = models.TextField()

