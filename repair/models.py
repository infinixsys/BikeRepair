import uuid
from ckeditor.fields import RichTextField
from django.db import models
from main.models import User


# Create your models here.


class AboutUs(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    img = models.ImageField(upload_to="aboutus/")
    short = models.TextField(default=None)
    details = RichTextField(default=None)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Services(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=400, blank=True, null=True)
    img = models.ImageField(upload_to="service/", blank=True, null=True)
    date = models.CharField(max_length=12, blank=True, null=True)
    order_id = models.CharField(max_length=200, default=uuid.uuid4, blank=True, unique=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class PlanName(models.Model):
    STATUS = (
        ('onetime', 'onetime'),
        ('yearly', 'yearly'),
        ('monthly', 'monthly'),
    )
    title = models.CharField(max_length=200, blank=True, null=True)
    pricing = models.IntegerField(blank=True, null=True)
    types = models.CharField(max_length=200, blank=True, null=True, choices=STATUS)
    details = RichTextField(default=None)
    img = models.ImageField(upload_to="plan_name/", blank=True, null=True)
    services = models.CharField(max_length=200, blank=True, null=True)
    card_details = models.CharField(max_length=200, blank=True, null=True)
    line_price = models.IntegerField(blank=True, null=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    notification = models.TextField(default=None)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.notification


class BookingDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    model = models.CharField(max_length=200, blank=True, null=True)
    vehicle_number = models.CharField(max_length=200, blank=True, null=True)
    year_of_purchase = models.CharField(max_length=200, blank=True, null=True)
    odometer_reading = models.CharField(max_length=200, blank=True, null=True)
    rc_number = models.CharField(max_length=200, blank=True, null=True)
    owner_name = models.CharField(max_length=200, blank=True, null=True)
    pin_code = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=300, blank=True, null=True)
    brand = models.CharField(max_length=200, blank=True, null=True)
    Vehicle_issues = models.TextField(default=None)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.model


class Order(models.Model):
    plane_name = models.ForeignKey(PlanName, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    order_amount = models.CharField(max_length=25)
    order_payment_id = models.CharField(max_length=100)
    isPaid = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plane_name.title


class ClientReview(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    img = models.ImageField(upload_to="img/", blank=True, null=True)
    txt = models.TextField(default=None)

    def __str__(self):
        return self.name
