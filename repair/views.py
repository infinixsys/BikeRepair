import json

import razorpay
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import AboutUs, Services, PlanName, Notification, Order, ClientReview, BookingDetails, Support, Service
from .serializers import AboutUsSerializer, ServiceSerializer, PlanNameSerializer, \
    NotificationSerializer, OrderSerializer, ClientReviewSerializer, BookingDetailsSerializer, PlanUpdateSerializer, \
    SupportSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from django.conf import settings
from repair.models import PlanUpdate


# Create your views here.


class AboutUsListView(ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class ServiceListAPI(ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer


class PlanNameListAPI(ListAPIView):
    queryset = PlanName.objects.all()
    serializer_class = PlanNameSerializer


class NotificationListAPI(ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class BookingDetailsAPIView(ListCreateAPIView):
    queryset = BookingDetails.objects.all()
    serializer_class = BookingDetailsSerializer


class BookingDeleteUpdateAPI(RetrieveDestroyAPIView, RetrieveUpdateAPIView):
    queryset = BookingDetails.objects.all()
    serializer_class = BookingDetailsSerializer


@api_view(['POST'])
def start_payment(request):
    amount = request.data['amount']
    plane_name = request.data['plane_name']

    client = razorpay.Client(auth=(settings.PUBLIC_KEY, settings.RAZOR_SECRET_KEY))

    payment = client.order.create({"amount": int(amount) * 100,
                                   "currency": "INR",
                                   "payment_capture": "1"})

    order = Order.objects.create(plane_name=plane_name,
                                 order_amount=amount,
                                 order_payment_id=payment['id'])

    serializer = OrderSerializer(order)

    data = {
        "payment": payment,
        "order": serializer.data
    }
    return Response(data)


@api_view(['POST'])
def handle_payment_success(request):
    # request.data is coming from frontend
    res = json.loads(request.data["response"])

    ord_id = ""
    raz_pay_id = ""
    raz_signature = ""

    for key in res.keys():
        if key == 'razorpay_order_id':
            ord_id = res[key]
        elif key == 'razorpay_payment_id':
            raz_pay_id = res[key]
        elif key == 'razorpay_signature':
            raz_signature = res[key]

    order = Order.objects.get(order_payment_id=ord_id)

    data = {
        'razorpay_order_id': ord_id,
        'razorpay_payment_id': raz_pay_id,
        'razorpay_signature': raz_signature
    }

    client = razorpay.Client(auth=(settings.PUBLIC_KEY, settings.RAZOR_SECRET_KEY))

    check = client.utility.verify_payment_signature(data)

    if check is not None:
        print("Redirect to error url or error page")
        return Response({'error': 'Something went wrong'})

    order.isPaid = True
    order.save()

    res_data = {
        'message': 'payment successfully received!'
    }

    return Response(res_data)


class OrderAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ClientReviewAPIView(ListCreateAPIView):
    queryset = ClientReview.objects.all()
    serializer_class = ClientReviewSerializer


class PlanUpdateAPIView(ListCreateAPIView):
    queryset = PlanUpdate.objects.all()
    serializer_class = PlanUpdateSerializer


class SuppportAPIView(ListCreateAPIView):
    queryset = Support.objects.all()
    serializer_class = SupportSerializer


class ServiceList(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def perform_create(self, serializer):
        if serializer.validated_data.get('service_type') == 'one-time':
            serializer.save(completed=False)
        else:
            serializer.save()


class ServiceDetail(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def perform_update(self, serializer):
        if serializer.validated_data.get('completed') and serializer.validated_data['service_type'] == 'one-time':
            serializer.validated_data['expires'] = None
        serializer.save()
