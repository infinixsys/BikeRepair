from django.shortcuts import render
from .models import *


# Create your views here.


def home(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            mobile = request.POST.get('phone')
            email = request.POST.get('email')
            city = request.POST.get('city')
            model = request.POST.get('model')
            phone = int(mobile)

            data = HomeBooking.objects.create(name=name, phone=phone, email=email, city=city, model=model)
            data.save()
            msg = "Your Details Has Been Successfully sent !"
            return render(request, 'home.html', {'msg': msg})
    except Exception as E:
        return render(request, 'home.html', {'msg': E})
    return render(request, 'home.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def contactus(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            mobile = request.POST.get('phone')
            email = request.POST.get('email')
            city = request.POST.get('city')
            model = request.POST.get('model')
            phone = int(mobile)
            data = HomeBooking.objects.create(name=name, phone=phone, email=email, city=city, model=model)
            data.save()
            msg = "Your Details Has Been Successfully sent !"
            return render(request, 'contactus.html', {'msg': msg})
    except Exception as E:
        return render(request, 'contactus.html', {'msg': E})
    return render(request, 'contactus.html')


def service(request):
    return render(request, 'service.html')


def privacy(request):
    return render(request, 'privacy-policy.html')


def terms(request):
    return render(request, 'terms-condition.html')
