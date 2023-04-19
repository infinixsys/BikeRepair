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
    rev = ClientReview.objects.all()
    return render(request, 'review.html', {'rev': rev})


def mechanice(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        profile = request.POST.get('profile')
        email = request.POST.get('email')
        price = request.POST.get('price')
        experiance = request.POST.get('experiance')
        number = request.POST.get('number')
        img = request.POST.get('img')
        data = Mechanic.objects.create(name=name, profile=profile, email=email, price=price, experiance=experiance,
                                       number=number, img=img)
        data.save()
        msg = "Your Detail Has Been Submitted !!"
        return render(request, 'addmechanic.html', {'msg': msg})
    return render(request, 'addmechanic.html')


def booking_leads(request):
    plane = PlanUpdate.objects.all()

    return render(request, 'booking_leads.html', {'plane': plane})


def booking_details(request, id):
    plane = PlanUpdate.objects.get(id=id)
    return render(request, 'booking-details.html', {'plane': plane})


def user_profile(request):
    plane = PlanUpdate.objects.all()
    # for i in plane:
    #     print(i.user.)
    return render(request, 'user_profile.html', {'plane': plane})


def user_history(request, id):
    plane = PlanUpdate.objects.get(id=id)
    return render(request, 'user-history.html', {'plane': plane})


def support(request):
    sup = Support.objects.all()
    return render(request, 'support.html', {'sup': sup})


def account(request):
    return render(request, 'account.html')


def bill_view(request):
    return render(request, 'bill-view.html')


def faq(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        data = FQA.objects.create(question=question, answer=answer)
        data.save()
        msg = "FQA is Added Successfully !!"
        return render(request, 'addfaq.html', {'msg': msg})
    return render(request, 'addfaq.html')


def banner(request):
    return render(request, 'banner.html')


def add_banner(request):
    return render(request, 'add-banner.html')


def offer_banner(reqeust):
    return render(reqeust, 'offer-banner.html')


def add_offer_banner(reqeust):
    return render(reqeust, 'add-offer-banner.html')
