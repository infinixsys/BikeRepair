from django.urls import path
from .views import *

urlpatterns = [
    path('adminpanel/', adminpanel, name='adminpanel'),
    path('addplan/', addplan, name='addplan'),
    path('plan', plan, name='plan'),
    path('editplan/<int:id>/', editplan, name='editplan'),
]