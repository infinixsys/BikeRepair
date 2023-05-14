import datetime
import uuid
from datetime import timezone

from ckeditor.fields import RichTextField
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from main.models import User

# Create your models here.

today = datetime.datetime.today()


class AboutUs(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    img = models.ImageField(upload_to="aboutus/")
    short = models.TextField(default=None)
    details = RichTextField(default=None)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


# class Services(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
#     title = models.CharField(max_length=400, blank=True, null=True)
#     img = models.ImageField(upload_to="service/", blank=True, null=True)
#     date = models.CharField(max_length=12, blank=True, null=True)
#     order_id = models.CharField(max_length=200, default=uuid.uuid4, blank=True, unique=True)
#     create_at = models.DateField(auto_now_add=True)
#     update_at = models.DateField(auto_now=True)
#
#     def __str__(self):
#         return self.title


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


class ClientReview(models.Model):
    STATUS = (
        ('approved', 'approved'),
        ('disapproved', 'disapproved'),
    )
    name = models.CharField(max_length=300, blank=True, null=True)
    img = models.ImageField(upload_to="img/", blank=True, null=True)
    txt = models.TextField(default=None)
    status = models.CharField(max_length=200, blank=True, null=True, choices=STATUS, default="disapproved")

    def __str__(self):
        return self.name


class PlanUpdate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    plane_name = models.ForeignKey(PlanName, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Support(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    contact = models.CharField(max_length=200, blank=True, null=True)
    txt = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name


class FQA(models.Model):
    question = models.CharField(max_length=500, blank=True, null=True)
    answer = RichTextField(default=None, blank=True, null=True)

    # def __str__(self):
    #     return self.question


class Mechanic(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    profile = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    price = models.CharField(max_length=200, blank=True, null=True, default=0)
    experiance = models.CharField(max_length=200, blank=True, null=True)
    number = models.CharField(max_length=200, blank=True, null=True)
    img = models.ImageField(upload_to="mechanic/", blank=True, null=True)
    aadhar = models.CharField(max_length=20, blank=True, null=True, default=0)
    upload_aadhar = models.FileField(upload_to="aadhar/", blank=True, null=True)
    resume = models.FileField(upload_to="resume/", blank=True, null=True)
    qualifications = models.CharField(max_length=200, blank=True, null=True)
    skills = models.CharField(max_length=200, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    STATUS = (
        ('onetime', 'onetime'),
        ('yearly', 'yearly'),
        ('monthly', 'monthly'),
    )
    plane_name = models.ForeignKey(PlanName, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    order_amount = models.CharField(max_length=25)
    order_payment_id = models.CharField(max_length=100)
    service_types = models.CharField(max_length=200, blank=True, null=True, choices=STATUS)
    count = models.IntegerField(blank=True, null=True)
    isPaid = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now=True)
    expiry_date = models.DateTimeField(blank=True, null=True)


@receiver(pre_save, sender=Order)
def update_active(sender, instance, *args, **kwargs):
    if instance.expiry_date == today:
        instance.isPaid = False
    else:
        instance.paid = True

    def __str__(self):
        return self.order_amount


class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    plan_title = models.CharField(max_length=200, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    bike = models.ForeignKey(BookingDetails, on_delete=models.CASCADE, blank=True, null=True)
    brand = models.CharField(max_length=200, blank=True, null=True)
    princing = models.CharField(max_length=200, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateField(auto_now=True, blank=True, null=True)
