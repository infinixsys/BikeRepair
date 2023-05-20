from unicodedata import decimal
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from main.models import *
from repair.models import *
from .models import *
from django.db.models import Q


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
                return redirect('plan')
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
                data.save()
                msg = "Your Plane Has Been Updated !"
                return redirect('plan')
            elif types == 'onetime' or types == 'monthly':
                data = PlanName.objects.get(id=id)
                data.title = title
                data.pricing = pricing
                data.types = types
                data.details = details
                data.save()
                msg = "Your Plane Has Been Updated !"
                return redirect('plan')
            elif img != None:
                data = PlanName.objects.get(id=id)
                data.title = title
                data.pricing = pricing
                data.types = types
                data.details = details
                data.img = img
                data.save()
                msg = "Your Plane Has Been Updated !"
                return redirect('plan')
            else:
                data = PlanName.objects.get(id=id)
                data.title = title
                data.pricing = pricing
                data.details = details
                data.save()
                msg = "Your Plane Has Been Updated !"
                return redirect('plan')

    except Exception as E:
        msg = E
        return render(request, 'addplan.html', {'msg': msg})
    return render(request, 'addplan.html', {'plans': plans})


def updateactive(request, id):
    plans = get_object_or_404(PlanName, id=id)
    status = "inactive"
    data = PlanName.objects.get(id=id)
    data.status = status
    data.save()
    return redirect('plan')


def updateinactive(request, id):
    plans = get_object_or_404(PlanName, id=id)
    status = "active"
    data = PlanName.objects.get(id=id)
    data.status = status
    data.save()
    return redirect('plan')


def deleteplan(request, id):
    instance = get_object_or_404(PlanName, id=id)
    instance.delete()
    return redirect('plan')


def review(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')

    rev = ClientReview.objects.all()
    data = request.GET.get('data')
    if data == "approved":
        rev = rev.filter(status=data)
    if data == "disapproved":
        rev = rev.filter(status=data)
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
    if request.method == 'POST':
        data = request.POST.get('data')
        plane = Order.objects.filter(
            Q(user__phone__icontains=data) | Q(user__email__icontains=data) | Q(user__fname__icontains=data))
        return render(request, 'booking_leads.html', {'plane': plane})
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
    if request.method == 'POST':
        data = request.POST.get('data')
        plane = User.objects.filter(Q(phone__icontains=data) | Q(fname__icontains=data) | Q(email__icontains=data))
        return render(request, 'user_profile.html', {'plane': plane})
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
    cls = ClientSupport.objects.all()
    return render(request, 'support.html', {'sup': sup, 'cls': cls})


def editsupport(request, id):
    cls = get_object_or_404(ClientSupport, id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        txt = request.POST.get('txt')
        cls = ClientSupport.objects.get(id=id)
        cls.name = name
        cls.contact = contact
        cls.txt = txt
        cls.save()
        return redirect('support')
    return render(request, 'editsupport.html', {'cls': cls})


def account(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    bc = BillCreate.objects.all().order_by('-id')
    if request.method == 'POST':
        pass
    return render(request, 'account.html', {'ords': bc})


def create_bill(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    ords = Order.objects.all()
    if request.method == 'POST':
        # order_id = request.POST.get('order')
        # order = Order.objects.get(id=order_id)
        bill_name = request.POST.get("bill_name", None)
        bill_company = request.POST.get("bill_company", None)
        bill_address = request.POST.get("bill_address", None)
        bill_pincode = request.POST.get("bill_pincode", None)
        bill_phone = request.POST.get("bill_phone", None)
        total_service = request.POST.get("total_service", None)
        tax = request.POST.get("tax", None)
        igst = request.POST.get("igst", None)
        sgst = request.POST.get("sgst", None)
        cgst = request.POST.get("cgst", None)
        txt = request.POST.get("txt", None)
        ship_name = request.POST.get('ship_name', None)
        ship_address = request.POST.get('ship_address', None)
        ship_pincode = request.POST.get('ship_pincode', None)
        ship_phone = request.POST.get('ship_phone', None)
        ship_gst = request.POST.get('ship_gst', None)
        item_name = request.POST.get('item_name', None)
        item_unit = request.POST.get('item_unit', None)
        item_quantity = request.POST.get('item_quantity', None)
        item_rate = request.POST.get('item_rate', None)
        if ship_gst is not None:
            ship = int(((int(item_unit)*int(item_quantity))*int(ship_gst))/100)
            total = ship + int(total_service)
            total = total
            data = BillCreate.objects.create(bill_name=bill_name, bill_company=bill_company,
                                             bill_address=bill_address
                                             , bill_pincode=bill_pincode, bill_phone=bill_phone,
                                             total_service=total_service,
                                             tax=tax, igst=igst, sgst=sgst, cgst=cgst, total=total, txt=txt,
                                             ship_name=ship_name, ship_address=ship_address, ship_pincode=ship_pincode,
                                             ship_phone=ship_phone, ship_gst=ship_gst, item_name=item_name,
                                             item_unit=item_unit, item_quantity=item_quantity, item_rate=item_rate)
            data.save()
            return redirect('account')
        else:
            total = total_service
            data = BillCreate.objects.create(bill_name=bill_name, bill_company=bill_company,
                                             bill_address=bill_address
                                             , bill_pincode=bill_pincode, bill_phone=bill_phone,
                                             total_service=total_service,
                                             tax=tax, igst=igst, sgst=sgst, cgst=cgst, total=total, txt=txt,
                                             ship_name=ship_name, ship_address=ship_address, ship_pincode=ship_pincode,
                                             ship_phone=ship_phone, ship_gst=ship_gst, item_name=item_name,
                                             item_unit=item_unit, item_quantity=item_quantity, item_rate=item_rate)
            data.save()
            return redirect('account')

    return render(request, 'create-bill.html', {'ords': ords})


def view_bill(request, id):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    invoice = BillCreate.objects.get(id=id)
    return render(request, 'view-bill.html', {'invoice': invoice})


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


def changeusername(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    if request.method == 'POST':
        old_phone = request.POST.get('old_phone')
        new_phone = request.POST.get('new_phone')
        user = User.objects.get(phone=request.user.phone)
        if user.phone == old_phone:
            user.phone = new_phone
            user.save()
            return redirect('login_attempt')
    return render(request, 'changeusername.html')


def changepassword(request):
    if not request.user.is_superuser:
        return redirect('login_attempt')
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        user = User.objects.get(phone=request.user.phone)
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return redirect('login_attempt')
    return render(request, 'changepassword.html')
