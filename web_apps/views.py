from django.shortcuts import render
from commo.models import Commo

def dashboard(request):
    commos = Commo.objects.order_by('-created_at')
    return render(commos, 'supder/dashboard.html', {'commos': commos})