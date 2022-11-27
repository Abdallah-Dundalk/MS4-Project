from django.shortcuts import render, redirect, get_object_or_404
from .models import AccessLog
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import AccessForm

import base64
import datetime

# Create your views here.


def get_home_page(request):
    return render(request, 'index.html')


def get_roll_call_page(request):
    items = AccessLog.objects.all().filter(on_site_status=True)
    context = {
        'items': items
    }
    
    return render(request, 'roll_call.html', context)


def get_access_log_page(request):
    logs = AccessLog.objects.all()
   
    for log in logs:
        if log.time_out is None:
            log.on_site_status = True
            log.save()
        else:
            log.on_site_status = False
            log.save()

    page = request.GET.get('page', 1)
    paginator = Paginator(logs, 30)

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    
    context = {
        'items': items
    }

    return render(request,'access_log.html', context)
   

def get_access_form_page(request):
    if request.method == 'POST':
        form = AccessForm(request.POST)
        if form.is_valid():
            form.save()
            print("form saved")
            messages.success(request, 'Delivery successfully logged.')
            
            return redirect('get_access_log')
    form = AccessForm()
    context = {
        'form': form
    }

    return render(request, 'access_form.html', context)

    
def get_search_page(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    company = request.POST.get('company')
    
    items = AccessLog.objects.all().filter(Q(first_name__iexact=first_name) | Q(last_name__iexact=last_name) | Q(company__iexact=company))
    context = {
            'items': items
        }
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        company = request.POST.get('company')
        items = AccessLog.objects.all().filter(Q(first_name__iexact=first_name) | Q(company__iexact=company) )
        context = {
            'items': items
            }
        if items:
            messages.info(request, 'Records found')
        else:
            messages.success(request, 'No records found')
    return render(request, 'search_page.html', context)


def edit_log_page(request, item_id):
    item = get_object_or_404(AccessLog, id=item_id)
    if request.method == 'POST':
        form = AccessForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record successfully update.')
            return redirect('get_access_log')
    form = AccessForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'edit_log.html', context)
    

    #  if request.method == 'POST' and 'default-submit-button' in request.POST:
    #     form = AccessForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         print("form saved")
    #         return redirect('get_access_log')
    # return render(request, 'access_log.html', context)


def edit_time_out_page(request, item_id):
    item = get_object_or_404(AccessLog, id=item_id)
    if request.method == 'POST' and 'time-out-submit-btn' in request.POST:
        item.time_out = datetime.datetime.now()
        item.save()
        # form = AccessForm(request.POST, instance=item)
        # if form.is_valid():
        #     form.save()
        
        messages.success(request, " 'Time Out' updated")
        return redirect('get_access_log')
    elif request.method == 'POST' and 'time-out-cancel-btn' in request.POST:
        
        messages.success(request, " 'Time Out' not updated")
        return redirect('get_access_log')
        
    form = AccessForm(instance=item)
    context = {
        
        'item': item
    }
    return render(request, 'edit_time_out.html', context)


def delete_log_page(request, item_id):
    item = get_object_or_404(AccessLog, id=item_id)
    if request.method == 'POST' and 'delete-btn' in request.POST:
        item.delete()
        print("deleted")
        messages.success(request, 'Record deleted.')
        return redirect('get_access_log')
    elif request.method == 'POST' and 'cancel-btn' in request.POST:
        print("cancelled")
        messages.success(request, 'Record not deleted.')
        return redirect('get_access_log')
    form = AccessForm(instance=item)
    context = {
        
        'item': item
    }
    return render(request, 'delete_record.html', context)