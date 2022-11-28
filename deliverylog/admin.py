from django.contrib import admin
from .models import AccessLog
# Register your models here.


@admin.register(AccessLog)
class AccessLogAdmin(admin.ModelAdmin):
    list_filter = ('created_on', 'company', 'officers_name', 'first_name',
                   'last_name', 'destination')
    list_display = ('first_name', 'last_name', 'company', 'phone_number',
                    'destination', 'created_on', 'officers_name', 'time_in',
                    'time_out', 'entry_date')
    search_fields = ['first_name', 'company', 'destination']
