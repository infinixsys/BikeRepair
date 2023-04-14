from rest_framework import serializers
from .models import Profile, User, PlanUpdate


# class UserUpdateSerializer()

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'mobile', 'image', 'name', 'address', 'location')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", 'mobile', 'image', 'name', 'address', 'location', 'plan')


class PlanUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanUpdate
        fields = ('id', 'user', 'plane_name', 'name', 'mobile_number', 'address', 'location')
