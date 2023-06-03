from django.db import models
from ckeditor.fields import RichTextField
import random
from repair.models import Order


# Create your models here.
class AddBanner(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    priority = models.CharField(max_length=200, blank=True, null=True)
    img = models.ImageField(upload_to="img/", blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)


class AddOfferBanner(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    priority = models.CharField(max_length=200, blank=True, null=True)
    img = models.ImageField(upload_to="img/", blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)


class Item(models.Model):
    item_name = models.CharField(max_length=200, blank=True, null=True)
    item_unit = models.CharField(max_length=200, blank=True, null=True)
    item_quantity = models.CharField(max_length=200, blank=True, null=True)
    item_rate = models.CharField(max_length=200, blank=True, null=True)

    create_at = models.DateTimeField(auto_now_add=True)


class BillCreate(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    bill_name = models.CharField(max_length=200, blank=True, null=True)
    bill_company = models.CharField(max_length=200, blank=True, null=True)
    bill_address = models.CharField(max_length=200, blank=True, null=True)
    bill_pincode = models.CharField(max_length=200, blank=True, null=True)
    bill_phone = models.CharField(max_length=200, blank=True, null=True)
    invoice = models.IntegerField(default=None, blank=True, null=True)
    total_service = models.CharField(max_length=200, blank=True, null=True)
    tax = models.CharField(max_length=200, blank=True, null=True)
    igst = models.CharField(max_length=200, blank=True, null=True)
    sgst = models.CharField(max_length=200, blank=True, null=True)
    cgst = models.CharField(max_length=200, blank=True, null=True)
    total = models.CharField(max_length=200, blank=True, null=True)
    txt = RichTextField(default=None, blank=True, null=True)

    ship_name = models.CharField(max_length=200, blank=True, null=True)
    ship_address = models.CharField(max_length=200, blank=True, null=True)
    ship_pincode = models.CharField(max_length=200, blank=True, null=True)
    ship_phone = models.CharField(max_length=200, blank=True, null=True)
    ship_gst = models.CharField(max_length=200, blank=True, null=True)

    item = models.ManyToManyField(Item, blank=True, null=True)

    create_at = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.invoice:
            self.invoice = self.generate_invoice_number()
        super().save(*args, **kwargs)

    def generate_invoice_number(self):
        invoice = random.randint(100000, 999999)
        return invoice
