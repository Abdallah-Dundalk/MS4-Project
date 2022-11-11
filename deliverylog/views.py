from django.shortcuts import render
from .models import AccessLog

# Create your views here.


def get_home_page(request):
    return render(request, 'index.html')


def get_access_log_page(request):
    items = AccessLog.objects.all()
    context = {
        'items': items
    }
    return render(request, 'access_log.html', context)


def get_access_form_page(request):
    return render(request, 'access_form.html')