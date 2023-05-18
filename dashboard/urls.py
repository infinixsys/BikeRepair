from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_attempt, name='login_attempt'),
    path('logout/', logout_view, name="logout_view"),
    path('adminpanel/', adminpanel, name='adminpanel'),
    
    path('addplan/', addplan, name='addplan'),
    path('plan', plan, name='plan'),
    path('editplan/<int:id>/', editplan, name='editplan'),
    path('deleteplan/<int:id>/', deleteplan, name='deleteplan'),

    path('booking/leads', booking_leads, name='booking_leads'),
    path('booking/details/<int:id>', booking_details, name='booking_details'),

    path('user/profile', user_profile, name='user_profile'),
    path('user/history/<int:id>', user_history, name='user_history'),
    path('add/service/<int:id>', addservice, name='addservice'),

    path('account', account, name='account'),
    path('bill/create', create_bill, name='create_bill'),
    path('bill/view/<int:id>/', view_bill, name='view_bill'),

    path('banner', banner, name='banner'),
    path('add/banner', add_banner, name='add_banner'),
    path('delete/banner/<int:pk>', delete_banner, name='delete_banner'),

    path('offer/banner', offer_banner, name='offer_banner'),
    path('add/offer/banner', add_offer_banner, name='add_offer_banner'),
    path('delete/offer/banner/<int:pk>', delete_offer_banner, name="delete_offer_banner"),

    path('mechanice', mechanice, name='mechanice'),
    path('mechanic/list', mechanic_list, name='mechanic_list'),
    path('mechanic/delete/<int:id>/', deletemechanic, name='deletemechanic'),
    path('mechanic/update/<int:id>/', updatemechanic, name='updatemechanic'),
    path('mechanic/view/<int:id>/', viewmechanic, name='viewmechanic'),

    path('faq', faq, name='faq'),
    path('support', support, name='support'),

    path('review', review, name='review'),
    path('update/review/<int:id>/', approvedreview, name='approvedreview'),
    path('delete/review/<int:id>/', deletereview, name='deletereview'),

    path('editsupport/<int:id>/', editsupport, name='editsupport'),

    path('change/password/', changepassword, name='changepassword'),
    path('change/username/', changeusername, name='changeusername'),

]
