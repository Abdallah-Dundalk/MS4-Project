from django import forms
from .models import AccessLog
from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput

import datetime


class AccessForm(forms.ModelForm):
    class Meta:
        model = AccessLog
        fields = '__all__'

        widgets = {
            'created_on': DateTimePickerInput(),
            'time_in': TimePickerInput(),
            'time_out': TimePickerInput(),
            'parking_time_limit': TimePickerInput(),
            'entry_date': DatePickerInput()
        }



        