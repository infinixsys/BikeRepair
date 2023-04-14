from unicodedata import decimal

from django.shortcuts import render, get_object_or_404
from main.models import *
from repair.models import *
from .models import *


# Create your views here.

def adminpanel(request):
    return render(request, 'adminpanel.html')


def addplan(request):
    try:
        if request.method == 'POST':
            title = request.POST.get('title')
            pricing_add = request.POST.get('pricing')
            types = request.POST.get('types')
            details = request.POST.get('details')
            img = request.FILES['img']
            pricing = int(pricing_add)
            if types == 'yearly':
                data = PlanName.objects.create(title=title, pricing=pricing, types=types, details=details, img=img,
                                               services='yearly')
                data.save()
                msg = "Your Plane Has Been Created !"
                return render(request, 'addplan.html', {'msg': msg})
            elif types == 'onetime':
                data = PlanName.objects.create(title=title, pricing=pricing, types=types, details=details, img=img,
                                               services="onetime")
                data.save()
                msg = "Your Plane Has Been Created !"
                return render(request, 'addplan.html', {'msg': msg})
            else:
                msg = "Something Went Wrong Please Select Correct Plan Name !"
                return render(request, 'addplan.html', {'msg': msg})
    except Exception as e:
        msg = "Something Went Wrong !"
        return render(request, 'addplan.html', {'msg': msg})
    return render(request, 'addplan.html')


def plan(request):
    plans = PlanName.objects.all()
    return render(request, 'plan.html', {'plans': plans})


def editplan(request, id):
    plans = get_object_or_404(PlanName, id=id)
    try:
        if request.method == 'POST':
            title = request.POST.get('title')
            pricing_add = request.POST.get('pricing')
            types = request.POST.get('types')
            details = request.POST.get('details')
            img = request.FILES['img']
            pricing = int(pricing_add)
            if types == 'yearly':
                data = PlanName.objects.get(id=id)
                data.title = title
                data.pricing = pricing
                data.types = types
                data.details = details
                data.img = img
                data.save()
                msg = "Your Plane Has Been Updated !"
                return render(request, 'addplan.html', {'msg': msg})
            elif types == 'onetime':
                data = PlanName.objects.get(id=id)
                data.title = title
                data.pricing = pricing
                data.types = types
                data.details = details
                data.img = img
                data.save()
                msg = "Your Plane Has Been Updated !"
                return render(request, 'addplan.html', {'msg': msg})
            else:
                msg = "Something Went Wrong Please Select Correct Plan Name !"
                return render(request, 'addplan.html', {'msg': msg})
    except Exception as e:
        msg = "Something Went Wrong !"
        return render(request, 'addplan.html', {'msg': msg})
    return render(request, 'addplan.html', {'plans': plans})


def review(request):
    return render(request, 'review.html')
