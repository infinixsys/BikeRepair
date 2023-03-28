import random

from django.contrib.auth import login
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import send_otp
from .models import Profile, User
from .serializers import UserUpdateSerializer, ProfileSerializer, UserSerializer, UserProfileSerializer


# Create your views here.

class RegisterView(APIView):
    @csrf_exempt
    def post(self, request, format=None):
        mobile = request.POST.get('mobile')

        check_user = User.objects.filter(mobile=mobile).first()
        check_profile = Profile.objects.filter(mobile=mobile).first()

        if check_user or check_profile:
            context = {'message': 'Mobile No. Already Exists!', 'class': 'danger'}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(username=mobile, mobile=mobile)
        user.save()
        otp = str(random.randint(999, 9999))
        profile = Profile(user=user, mobile=mobile, otp=otp)
        profile.save()
        # send_otp(mobile, otp)
        request.session['mobile'] = mobile
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def otp(request):
    mobile = request.session.get('mobile')
    if not mobile:
        return Response({'message': 'Mobile number not found in session'}, status=status.HTTP_400_BAD_REQUEST)

    otp = request.data.get('otp')
    profile = Profile.objects.filter(mobile=mobile).first()

    if not profile:
        return Response({'message': 'Profile not found for the given mobile number'}, status=status.HTTP_404_NOT_FOUND)

    if otp == profile.otp:
        return Response({'message': 'OTP verification successful', "is_verified": True}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Wrong OTP', "is_verified": False}, status=status.HTTP_401_UNAUTHORIZED)


class LoginAttemptView(APIView):
    def post(self, request):
        mobile = request.POST.get('mobile')

        user = Profile.objects.filter(mobile=mobile).first()

        if user is None:
            return Response({'message': 'User not found', 'class': 'danger'}, status=status.HTTP_400_BAD_REQUEST)

        otp = str(random.randint(1000, 9999))
        user.otp = otp
        user.save()
        send_otp(mobile, otp)
        request.session['mobile'] = mobile
        return Response(status=status.HTTP_302_FOUND)


class LoginOtpView(APIView):
    def get(self, request):
        mobile = request.session['mobile']
        context = {'mobile': mobile}
        return Response(context)

    def post(self, request):
        mobile = request.session['mobile']
        otp = request.data.get('otp')
        profile = Profile.objects.filter(mobile=mobile).first()

        if otp == profile.otp:
            user = User.objects.get(id=profile.user.id)
            login(request, user)
            return Response(status=status.HTTP_302_FOUND)
        else:
            context = {'message': 'Wrong OTP', 'class': 'danger', 'mobile': mobile}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)


class UserRetrieveUpdateAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserUpdateSerializer

    def put(self, request, user_id, format=None):
        user = User.objects.get(id=user_id)
        serializer = UserUpdateSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfile(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer


