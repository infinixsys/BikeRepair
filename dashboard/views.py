from unicodedata import decimal

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from main.models import *
from repair.models import *
from .models import *


# Create your views here.
def adminpanel(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    return render(request, 'adminpanel.html')


def addplan(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
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
    if not request.user.is_superuser:
        return redirect('login_attempt')
    plans = PlanName.objects.all()
    return render(request, 'plan.html', {'plans': plans})


def editplan(request, id):
    if not request.user.is_superuser:
        return redirect('login_attempt')
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
    if not request.user.is_superuser:
        return redirect('login_attempt')
    rev = ClientReview.objects.all()
    return render(request, 'review.html', {'rev': rev})


def mechanice(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
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
    if not request.user.is_superuser:
        return redirect('login_attempt')
    plane = PlanUpdate.objects.all()
    return render(request, 'booking_leads.html', {'plane': plane})


def booking_details(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    # plane = PlanUpdate.objects.get(id=id)
    return render(request, 'booking-details.html')


def user_profile(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    plane = PlanUpdate.objects.all()
    # for i in plane:
    #     print(i.user.)
    return render(request, 'user_profile.html', {'plane': plane})


def user_history(request, id):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    plane = PlanUpdate.objects.get(id=id)
    return render(request, 'user-history.html', {'plane': plane})


def support(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    sup = Support.objects.all()
    return render(request, 'support.html', {'sup': sup})


def account(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    return render(request, 'account.html')


def create_bill(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    return render(request, 'create-bill.html')


def view_bill(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    return render(request, 'view-bill.html')


def faq(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    if request.method == 'POST':
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        data = FQA.objects.create(question=question, answer=answer)
        data.save()
        msg = "FQA is Added Successfully !!"
        return render(request, 'addfaq.html', {'msg': msg})
    return render(request, 'addfaq.html')


def banner(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    ban = AddBanner.objects.all()
    return render(request, 'banner.html', {'ban': ban})


def add_banner(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    if request.method == "POST":
        title = request.POST.get('title')
        priority = request.POST.get('priority')
        img = request.FILES['img']
        data = AddBanner.objects.create(title=title, priority=priority, img=img)
        data.save()
        msg = "Your Banner Added Successfully !!"
        return render(request, 'add-banner.html', {'msg': msg})
    return render(request, 'add-banner.html')


def delete_banner(request, pk):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    instance = AddBanner.objects.get(pk=pk)
    instance.delete()
    msg = "Your Images is Deleted !"
    return render(request, 'banner.html', {'msg': msg})


def offer_banner(reqeust):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    offban = AddOfferBanner.objects.all()
    return render(reqeust, 'offer-banner.html', {'offban': offban})


def add_offer_banner(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    if request.method == "POST":
        title = request.POST.get('title')
        priority = request.POST.get('priority')
        img = request.FILES['img']
        data = AddOfferBanner.objects.create(title=title, priority=priority, img=img)
        data.save()
        msg = "Your Banner Added Successfully !!"
        return render(request, 'add-offer-banner.html', {'msg': msg})
    return render(request, 'add-offer-banner.html')


def delete_offer_banner(request, pk):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    instance = AddOfferBanner.objects.get(pk=pk)
    instance.delete()
    msg = "Your Images is Deleted !"
    return render(request, 'offer-banner.html', {'msg': msg})


def login_attempt(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(request, phone=phone, password=password)
        if user is not None:
            login(request, user)
            return redirect('adminpanel')
        else:
            msg = "Invalid Credential please check phone no. or password !!"
            return render(request, 'login_attempt.html', {'msg':msg})
    return render(request, 'login_attempt.html')
