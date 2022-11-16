from django.shortcuts import render, redirect
from .models import AccessLog
import base64

# Create your views here.


def get_home_page(request):
    return render(request, 'index.html')


def get_access_log_page(request):
    items = AccessLog.objects.all()
    context = {
        'items': items
    }
    for item in items:
        if item.time_out is None:
            item.on_site_status = True
        else:
            item.on_site_status = False
    return render(request, 'access_log.html', context)


def get_access_form_page(request):
    if request.method == 'POST':
        
        gate_number = request.POST.get('gate_number')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        passenger1_first_name = request.POST.get('passenger1_first_name')
        passenger1_last_name = request.POST.get('passenger1_last_name')
        passenger2_first_name = request.POST.get('passenger2_first_name')
        passenger2_last_name = request.POST.get('passenger2_last_name')
        passenger3_first_name = request.POST.get('passenger3_first_name')
        passenger3_last_name = request.POST.get('passenger3_last_name')
        passenger4_first_name = request.POST.get('passenger4_first_name')
        passenger4_last_name = request.POST.get('passenger4_last_name')
        phone_number = request.POST.get('phone_number')
        registration = request.POST.get('registration')
        company = request.POST.get('company')
        destination = request.POST.get('destination')
        parking_time_limit = request.POST.get('parking_time_limit')
        officers_name = request.POST.get('officers_name')
        signature = request.POST.get('signature')
        time_in = request.POST.get('time_in')
        time_out = None
        entry_date = request.POST.get('entry_date')
        parking_time_limit = request.POST.get('parking_time_limit')
        created_on = request.POST.get('created_on')
        
        AccessLog.objects.create(signature=signature, created_on=created_on, time_in=time_in, time_out=time_out, entry_date=entry_date, gate_number=gate_number, first_name=first_name, last_name=last_name, passenger1_first_name=passenger1_first_name, passenger1_last_name=passenger1_last_name, passenger2_first_name=passenger2_first_name, passenger2_last_name=passenger2_last_name, passenger3_first_name=passenger3_first_name, passenger3_last_name=passenger3_last_name, passenger4_first_name=passenger4_first_name, passenger4_last_name=passenger4_last_name, phone_number=phone_number, registration=registration, company=company, destination=destination, parking_time_limit=parking_time_limit, officers_name=officers_name)

        return redirect('get_access_log')
    return render(request, 'access_form.html')