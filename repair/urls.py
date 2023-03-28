from django.urls import path
from .views import *

urlpatterns = [
    path('api/about/us/', AboutUsListView.as_view(), name='about_us'),
    path('api/service/list/', ServiceListAPI.as_view(), name='service'),
    path('api/plan/list/', PlanNameListAPI.as_view(), name='plan_name'),
    path('api/notification/list/', NotificationListAPI.as_view(), name='notification'),
    path('api/add/booking/details/', BookingDetailsAPIView.as_view(), name='add_vehicle'),

    path('pay/', start_payment, name="payment"),
    path('payment/success/', handle_payment_success, name="payment_success"),

    path('order/details/', OrderAPIView.as_view(), name='OrderAPIView'),
    path('api/client/review', ClientReviewAPIView.as_view(), name='client_review'),
]