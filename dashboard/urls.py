from django.urls import path
from .views import *

urlpatterns = [
    path('adminpanel/', adminpanel, name='adminpanel'),
    path('addplan/', addplan, name='addplan'),
    path('plan', plan, name='plan'),
    path('editplan/<int:id>/', editplan, name='editplan'),

    path('booking/leads', booking_leads, name='booking_leads'),
    path('booking/details', booking_details, name='booking_details'),

    path('user/profile', user_profile, name='user_profile'),
    path('user/history/<int:id>', user_history, name='user_history'),

    path('account', account, name='account'),
    path('bill/create', create_bill, name='create_bill'),
    path('bill/view', view_bill, name='view_bill'),

    path('banner', banner, name='banner'),
    path('add/banner', add_banner, name='add_banner'),
    path('delete/banner/<int:pk>', delete_banner, name='delete_banner'),

    path('offer/banner', offer_banner, name='offer_banner'),
    path('add/offer/banner', add_offer_banner, name='add_offer_banner'),
    path('delete/offer/banner/<int:pk>', delete_offer_banner, name="delete_offer_banner"),

    path('faq', faq, name='faq'),
    path('support', support, name='support'),
    path('mechanice', mechanice, name='mechanice'),
    path('review', review, name='review'),

]
