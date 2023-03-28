from unicodedata import decimal

from django.shortcuts import render
from main.models import *
from repair.models import *
from .models import *


# Create your views here.

def adminpanel(request):
    return render(request, 'adminpanel.html')


def addservice(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        pricing_add = request.POST.get('pricing')
        types = request.POST.get('types')
        details = request.POST.get('details')
        img = request.FILES['img']
        pricing = int(pricing_add)
        data = PlanName.objects.create(title=title, pricing=pricing, types=types, details=details, img=img)
        data.save()
        msg = "Your Plane Has Been Created !"
        return render(request, 'addservice.html', {'msg': msg})
    return render(request, 'addservice.html')
