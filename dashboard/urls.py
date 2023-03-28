from django.urls import path
from .views import *

urlpatterns = [
    path('adminpanel', adminpanel, name='adminpanel'),
    path('addservice', addservice, name='addservice'),
]