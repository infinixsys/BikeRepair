from django.urls import path
from .views import *

urlpatterns = [
    path('api/about/us/', AboutUsListView.as_view(), name='about_us'),
    path('api/service/list/', ServiceListAPI.as_view(), name='service'),
    path('api/plan/list/', PlanNameListAPI.as_view(), name='plan_name'),
    path('api/notification/list/', NotificationListAPI.as_view(), name='notification'),
    path('api/add/booking/details/', BookingDetailsAPIView.as_view(), name='add_vehicle'),

    path('pay/<int:pk>', start_payment, name="payment"),
    path('payment/success/', handle_payment_success, name="payment_success"),

    path('order/details/', OrderAPIView.as_view(), name='OrderAPIView'),
    path('api/client/review', ClientReviewAPIView.as_view(), name='client_review'),
    path('api/user/plan/update/', PlanUpdateAPIView.as_view(), name='PlanUpdateAPIView'),
    path('api/order/details/', OrderGetAPIView.as_view(), name='OrderGetAPIView'),

    path('api/support/', SuppportAPIView.as_view(), name='SuppportAPIView'),
    path('api/update/delete/booking/bikes/<int:pk>', BookingDeleteUpdateAPI.as_view(), name='BookingDeleteUpdateAPI'),

    path('api/service/data/', ServiceAPIView.as_view(), name='ServiceAPIView'),
    # path('api/service/details/<int:pk>', ServiceDetail.as_view(), name='ServiceDetail')
]