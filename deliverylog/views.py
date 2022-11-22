from django.shortcuts import render, redirect, get_object_or_404
from .models import AccessLog
from django.db.models import Q
from django.contrib import messages
from .forms import AccessForm
import base64

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
    items = AccessLog.objects.all()
    context = {
        'items': items
    }
    for item in items:
        if item.time_out is None:
            item.on_site_status = True
        else:
            item.on_site_status = False
            item.save()
    return render(request, 'access_log.html', context)


def get_access_form_page(request):
    if request.method == 'POST':
        form = AccessForm(request.POST)
        if form.is_valid():
            form.save()
            print("form saved")
            return redirect('get_access_log')

    form = AccessForm()
    context = {
        'form': form
    }
    
    return render(request, 'access_form.html', context)

    
def get_search_page(request):
    first_name = request.POST.get('first_name')
    company = request.POST.get('company')
    items = AccessLog.objects.all().filter(Q(first_name__iexact=first_name) | Q(company__iexact=company))
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
        messages.success(request, 'Comment posted')
    return render(request, 'search_page.html', context)


def edit_log_page(request, item_id):
    item = get_object_or_404(AccessLog, id=item_id)
    if request.method == 'POST':
        form = AccessForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_access_log')
    form = AccessForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'edit_log.html', context)