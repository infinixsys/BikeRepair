from rest_framework import serializers
from .models import *


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ('id', "title", 'img', 'short', 'details')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ('id', 'user', 'title', 'img', 'date', 'order_id')


class PlanNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanName
        fields = ('id', 'title', 'pricing', 'types', 'details', 'card_details', 'line_price')


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'user', 'notification')


class BookingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingDetails
        fields = ("id", "user", "model", "vehicle_number", "year_of_purchase", "odometer_reading", "rc_number",
                  "owner_name", "pin_code", "location", "Vehicle_issues", "brand")


class OrderSerializer(serializers.ModelSerializer):
    order_date = serializers.DateTimeField(format="%d %B %Y %I:%M %p")

    class Meta:
        model = Order
        fields = '__all__'
        depth = 2


class ClientReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientReview
        fields = "__all__"


class PlanUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanUpdate
        fields = ('id', 'user', 'plane_name', 'name', 'mobile_number', 'address', 'location')


class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    bike = BookingDetailsSerializer()
    expired = serializers.SerializerMethodField()
    completed = serializers.SerializerMethodField()
    message = serializers.SerializerMethodField()

    def get_expired(self, obj):
        return obj.expires and obj.expires < timezone.now()

    def get_completed(self, obj):
        if obj.service_type == 'one-time':
            return obj.completed
        return None

    def get_message(self, obj):
        if obj.service_type == 'four-times' and not obj.completed:
            remaining = obj.remaining_services()
            return f'{remaining} services remaining. Please book another service before the expiry date.'
        return None

    class Meta:
        model = Service
        fields = '__all__'
