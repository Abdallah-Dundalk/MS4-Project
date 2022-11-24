"""sentry_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from deliverylog.views import get_home_page, get_access_log_page, get_access_form_page, get_roll_call_page, get_search_page, edit_log_page, edit_time_out_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_home_page, name='get_home_page'),
    path('access_log/', get_access_log_page, name='get_access_log'),
    path('access_form/', get_access_form_page, name='get_access_form'),
    path('roll_call/', get_roll_call_page, name='get_roll_call'),
    path('search_page/', get_search_page, name='get_search_page'),
    path('access_log/edit_log/<item_id>/', edit_log_page, name='edit_log'),
    path('access_log/edit_time_out/<item_id>/', edit_time_out_page, name='edit_time_out_page'),
    path('accounts/', include('allauth.urls'))
]
