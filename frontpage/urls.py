from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('aboutus/', aboutus, name='aboutus'),
    path('contactus/', contactus, name='contactus'),
    path('service/', service, name='service'),
    path('privacy/', privacy, name='privacy'),
    path('terms/', terms, name='terms'),

]