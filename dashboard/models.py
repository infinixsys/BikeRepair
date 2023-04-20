from django.db import models


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

