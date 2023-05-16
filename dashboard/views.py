from unicodedata import decimal

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from main.models import *
from repair.models import *
from .models import *


# Create your views here.

def login_attempt(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(request, phone=phone, password=password)
        if user is not None:
            login(request, user)
            return redirect('adminpanel')
        else:
            msg = "Invalid Credential please check phone no. or password !!"
            return render(request, 'login_attempt.html', {'msg': msg})
    return render(request, 'login_attempt.html')


def logout_view(request):
    logout(request)
    return redirect('login_attempt')


def adminpanel(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    total_service = Service.objects.all().count()
    annul_service = Service.objects.filter(plan_title="annual").count()
    onetime_service = Service.objects.filter(plan_title="monthly").count()
    today_total_service = Service.objects.all().filter(create_at=datetime.datetime.today()).count()
    today_annul_service = Service.objects.filter(plan_title="annual").filter(
        create_at=datetime.datetime.today()).count()
    today_onetime_service = Service.objects.filter(plan_title="monthly").filter(
        create_at=datetime.datetime.today()).count()
    print(total_service)
    return render(request, 'adminpanel.html', {'total_service': total_service, 'annul_service': annul_service,
                                               'onetime_service': onetime_service,
                                               'today_total_service': today_total_service,
                                               'today_annul_service': today_annul_service,
                                               'today_onetime_service': today_onetime_service})


def plan(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    plans = PlanName.objects.all()
    return render(request, 'plan.html', {'plans': plans})


def addplan(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    try:
        if request.method == 'POST':
            title = request.POST.get('title')
            pricing_add = request.POST.get('pricing')
            types = request.POST.get('types')
            details = request.POST.get('details')
            img = request.FILES.get('img')
            pricing = int(pricing_add)
            if types == 'yearly':
                data = PlanName.objects.create(title=title, pricing=pricing, types=types, details=details, img=img,
                                               services='yearly')
                data.save()
                msg = "Your Plane Has Been Created !"
                return redirect('plan')
            elif types == 'onetime' or types == 'monthly':
                data = PlanName.objects.create(title=title, pricing=pricing, types=types, details=details, img=img,
                                               services="onetime")
                data.save()
                msg = "Your Plane Has Been Created !"
                return render(request, 'addplan.html', {'msg': msg})
            else:
                msg = "Something Went Wrong Please Select Correct Plan Name !"
                return render(request, 'addplan.html', {'msg': msg})
    except Exception as E:
        msg = E
        return render(request, 'addplan.html', {'msg': msg})
    return render(request, 'addplan.html')


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
            img = request.FILES.get('img')
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
            elif types == 'onetime' or types == 'monthly':
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
    except Exception as E:
        msg = E
        return render(request, 'addplan.html', {'msg': msg})
    return render(request, 'addplan.html', {'plans': plans})


def deleteplan(request, id):
    instance = get_object_or_404(PlanName, id=id)
    instance.delete()
    return redirect('plan')


def review(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    rev = ClientReview.objects.all()
    return render(request, 'review.html', {'rev': rev})


def approvedreview(request, id):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    update = get_object_or_404(ClientReview, id=id)
    status = "approved"
    instance = ClientReview.objects.get(id=id)
    instance.status = status
    instance.save()
    return redirect('review')


def deletereview(request, id):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    instance = get_object_or_404(ClientReview, id=id)
    instance.delete()
    return redirect('review')


def mechanic_list(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    ml = Mechanic.objects.all()
    return render(request, 'mechanic_list.html', {'ml': ml})


def mechanice(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    if request.method == 'POST':
        name = request.POST.get('name', None)
        profile = request.POST.get('profile', None)
        email = request.POST.get('email', None)
        price = request.POST.get('price', None)
        experiance = request.POST.get('experiance', None)
        number = request.POST.get('number', None)
        img = request.FILES.get('img', None)
        aadhar = request.POST.get('aadhar', None)
        upload_aadhar = request.FILES.get('upload_aadhar', None)
        resume = request.FILES.get('resume', None)
        qualifications = request.POST.get('qualifications', None)
        skills = request.POST.get('skills', None)

        data = Mechanic.objects.create(name=name, profile=profile, email=email, price=price, experiance=experiance,
                                       aadhar=aadhar, upload_aadhar=upload_aadhar, resume=resume,
                                       qualifications=qualifications,
                                       skills=skills,
                                       number=number, img=img)
        data.save()
        msg = "Your Detail Has Been Submitted !!"
        return redirect('mechanic_list')
    return render(request, 'addmechanic.html')


def deletemechanic(request, id):
    instance = get_object_or_404(Mechanic, id=id)
    instance.delete()
    return redirect('mechanic_list')


def updatemechanic(request, id):
    instance = get_object_or_404(Mechanic, id=id)
    if request.method == 'POST':
        name = request.POST.get('name', None)
        profile = request.POST.get('profile', None)
        email = request.POST.get('email', None)
        price = request.POST.get('price', None)
        experiance = request.POST.get('experiance', None)
        number = request.POST.get('number', None)
        img = request.FILES.get('img', None)
        aadhar = request.POST.get('aadhar', None)
        upload_aadhar = request.FILES.get('upload_aadhar', None)
        resume = request.FILES.get('resume', None)
        qualifications = request.POST.get('qualifications', None)
        skills = request.POST.get('skills', None)
        data = Mechanic.objects.get(id=id)
        data.name = name
        data.profile = profile
        data.email = email
        data.price = price
        data.experiance = experiance
        data.number = number
        data.img = img
        data.aadhar = aadhar
        data.upload_aadhar = upload_aadhar
        data.resume = resume
        data.qualifications = qualifications
        data.skills = skills
        data.save()
        return redirect('mechanic_list')
    return render(request, 'addmechanic.html', {'instance': instance})


def viewmechanic(request, id):
    instance = get_object_or_404(Mechanic, id=id)
    return render(request, 'mechanic.html', {'instance': instance})


def booking_leads(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    plane = Order.objects.all().order_by('-id')
    return render(request, 'booking_leads.html', {'plane': plane})


def booking_details(request, id):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    order = Order.objects.get(id=id)
    mechnic = Mechanic.objects.all()
    return render(request, 'booking-details.html', {'order': order, 'mechnic': mechnic})


def addservice(request, id):
    order = Order.objects.get(id=id)
    if order.isPaid:
        if order.service_types == 'onetime' or order.service_types == 'monthly':
            order.isPaid = False
            order.count -= 1
            order.save()
            value = Service.objects.create(user=order.user, order=order, bike=order.bookingdetails,
                                           brand=order.bookingdetails.brand,
                                           count=order.count,
                                           princing=order.order_amount, name=order.user.fname,
                                           username=order.user.phone,
                                           plan_title=order.plane_name.title)
            value.save()
            msg = "One Time Are Completed!"
            return redirect('booking_leads')
        elif order.service_types == "yearly":

            order.count -= 1
            order.save()
            if order.count == 0:
                order.isPaid = False
                order.save()
            value = Service.objects.create(user=order.user, order=order, bike=order.bookingdetails,
                                           brand=order.bookingdetails.brand,
                                           count=order.count,
                                           princing=order.order_amount, name=order.user.fname,
                                           username=order.user.phone,
                                           plan_title=order.plane_name.title)

            value.save()
            msg = "Service Order Are Completed"
            return redirect('booking_leads')
        else:
            msg = "Something Went Wrong"
            return render(request, 'booking_leads.html', {'msg': msg})
    else:
        msg = "Not Valid your Service ! Repayment Booking"
        return render(request, 'booking_leads.html', {'msg': msg})


def user_profile(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    plane = User.objects.all()
    # for i in plane:
    #     print(i.user.)
    return render(request, 'user_profile.html', {'plane': plane})


def user_history(request, id):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    plane = User.objects.get(id=id)
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


def offer_banner(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    offban = AddOfferBanner.objects.all()
    return render(request, 'offer-banner.html', {'offban': offban})


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
