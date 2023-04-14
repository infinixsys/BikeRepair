import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class User(AbstractUser):
    # id = models.CharField(max_length=200, primary_key=True, default=uuid.uuid4, editable=False)
    mobile = models.CharField(max_length=200, blank=True, null=True, unique=True)
    image = models.ImageField(upload_to="Profile/")
    name = models.CharField(max_length=300, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    plan = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    mobile = models.CharField(max_length=20)
    otp = models.CharField(max_length=6)

    def __str__(self):
        return self.mobile + '| ' + self.user.username


class PlanUpdate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    plane_name = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name