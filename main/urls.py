from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register_view'),
    path('api/register/otp/', otp, name="otp_register"),
    path('api/login/attempt/', LoginAttemptView.as_view(), name='login_attempt'),
    path('api/login/otp/', LoginOtpView.as_view(), name='login_otp'),
    path('api/user/update/<int:user_id>', UserRetrieveUpdateAPIView.as_view(), name='user_update'),
    path('api/user/profile/<int:pk>', UserProfile.as_view(), name="user_profile"),

]

