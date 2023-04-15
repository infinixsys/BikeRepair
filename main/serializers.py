import imp
from rest_framework import serializers
from .models import Profile, User, PlanUpdate, Role
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

# class UserUpdateSerializer()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "fname", "lname", "phone" ,"email","address","city","state","country","image","image"]
        extra_kwargs = {
            "id": {"read_only": True},
            # "fname": {"required": True},
            # "lname": {"required": True},
            "phone": {"required": True},
            # "email": {"required": True},
        }


    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user


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
