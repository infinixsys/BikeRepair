import json
import razorpay
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import User
from .models import AboutUs, Services, PlanName, Notification, Order, ClientReview, BookingDetails, Support, Service
from .serializers import AboutUsSerializer, ServiceSerializer, PlanNameSerializer, \
    NotificationSerializer, OrderSerializer, ClientReviewSerializer, BookingDetailsSerializer, PlanUpdateSerializer, \
    SupportSerializer, ServiceDataSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from django.conf import settings
from repair.models import PlanUpdate

from datetime import datetime, timedelta


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


# @login_required
@api_view(['POST'])
def start_payment(request, pk):
    plane_name = get_object_or_404(PlanName, pk=pk)
    user = request.user
    amount = plane_name.pricing

    client = razorpay.Client(auth=(settings.PUBLIC_KEY, settings.RAZOR_SECRET_KEY))

    payment = client.order.create({"amount": int(amount) * 100,
                                   "currency": "INR",
                                   "payment_capture": "1"})

    if plane_name.types == 'monthly':
        expiry_date = datetime.now() + timedelta(days=30)
        order = Order.objects.create(plane_name=plane_name, user=user, service_types='monthly',
                                     order_amount=amount, expiry_date=expiry_date, count=1,
                                     order_payment_id=payment['id'])
        serializer = OrderSerializer(order)
        data = {
            "payment": payment,
            "order": serializer.data,
        }
        return Response(data)

    if plane_name.types == 'onetime':
        expiry_date = datetime.now() + timedelta(days=30)

        order = Order.objects.create(plane_name=plane_name, user=user, service_types='onetime',
                                     order_amount=amount, expiry_date=expiry_date, count=1,
                                     order_payment_id=payment['id'])
        serializer = OrderSerializer(order)
        data = {
            "payment": payment,
            "order": serializer.data,
        }
        return Response(data)

    elif plane_name.types == 'yearly':
        expiry_date = datetime.now() + timedelta(days=365)

        order = Order.objects.create(plane_name=plane_name, user=user, service_types='yearly',
                                     order_amount=amount, expiry_date=expiry_date, count=4,
                                     order_payment_id=payment['id'])

        serializer = OrderSerializer(order)
        data = {
            "payment": payment,
            "order": serializer.data,
        }
        return Response(data)
    return Response({"status": False}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def handle_payment_success(request):
    # request.data is coming from frontend
    # print("response", " ===========================")
    # res = json.loads(request.data["response"])
    # print(res, "======================")
    # ord_id = ""
    # raz_pay_id = ""
    # raz_signature = ""
    #
    # for key in res.keys():
    #     if key == 'razorpay_order_id':
    #         ord_id = res[key]
    #     elif key == 'razorpay_payment_id':
    #         raz_pay_id = res[key]
    #     elif key == 'razorpay_signature':
    #         raz_signature = res[key]

    # if request.method == 'POST':
    ord_id = request.data["razorpay_order_id"]
    raz_pay_id = request.data["razorpay_payment_id"]
    raz_signature = request.data["razorpay_signature"]

    order = Order.objects.get(order_payment_id=ord_id)

    data = {
        'razorpay_order_id': ord_id,
        'razorpay_payment_id': raz_pay_id,
        'razorpay_signature': raz_signature
    }
    client = razorpay.Client(auth=(settings.PUBLIC_KEY, settings.RAZOR_SECRET_KEY))

    check = client.utility.verify_payment_signature(data)
    print(check, "=====================================")
    if check is None:
        print("Redirect to error url or error page")
        return Response({'error': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)

    order.isPaid = True
    order.save()

    res_data = {
        'message': 'payment successfully received!'
    }

    return Response(res_data, status=status.HTTP_200_OK)


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


# class ServiceList(ListCreateAPIView):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer
#
#     def perform_create(self, serializer):
#         if serializer.validated_data.get('service_type') == 'one-time':
#             serializer.save(completed=False)
#         else:
#             serializer.save()
#
#
# class ServiceDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer
#
#     def perform_update(self, serializer):
#         if serializer.validated_data.get('completed') and serializer.validated_data['service_type'] == 'one-time':
#             serializer.validated_data['expires'] = None
#         serializer.save()


class ServiceAPIView(APIView):

    def get(self, request):
        service = Service.objects.filter(user__id=request.user.id)
        serializer = ServiceDataSerializer(service, many=True)
        return Response(serializer.data)

    def post(self, request, formate=None):
        # serializer = ServiceDataSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = request.user
            order_id = request.data['order_id']
            order = Order.objects.get(id=order_id)
            booking_id = request.data['booking_id']
            booking = BookingDetails.objects.get(id=booking_id)
            if user != booking.user:
                return Response({'error': "user or booking Id Not Valid !"}, status=status.HTTP_400_BAD_REQUEST)
            if user != order.user:
                return Response({'error': "user or Order Id Not Valid !"}, status=status.HTTP_400_BAD_REQUEST)
            if order.isPaid:
                if order.service_types == 'onetime' or order.service_types == 'monthly':
                    data = Service.objects.create(user=user, order=order, bike=booking)
                    data.save()
                    return Response({'success': "One Time Are Completed!"}, status=status.HTTP_200_OK)
                if order.service_types == "yearly":
                    data = Service.objects.create(user=user, order=order, bike=booking)
                    data.save()
                    return Response({'success': "First Time Are Completed!"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "First completed your Payment", "order_id": order.isPaid},
                                status=status.HTTP_400_BAD_REQUEST)

        except Exception as E:
            return Response({"Error": "Something Went Wrong! Please Login"}, status=status.HTTP_400_BAD_REQUEST)


class OrderGetAPIView(APIView):
    def get(self, request, *args, **kwargs):
        ord = Order.objects.filter(user__id=request.user.id)
        serializer = OrderSerializer(ord, many=True)
        return Response(serializer.data)
