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
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'company': 'Company',
            'phone_number': 'Phone Number',
            'registration': 'Registration',
            'create_on': 'Created On',
            'entry_date': 'Date',
            'destination': 'Destination',
            'time_in': 'Time In',
            'time_out': 'Time Out',
            'signature': 'Signature',
            'parking_time_limit': 'Parking Time Limit',
            'officers_name': 'Officer Name',
            'gate_number': 'Gate Number',
            'last_name': 'Last Name',
            'passenger1_first_name': 'Passenger 1 First Name',
            'passenger1_last_name': 'Passenger 1 Last Name',
            'passenger2_first_name': 'Passenger 2 First Name',
            'passenger2_last_name': 'Passenger 2 Last Name',
            'passenger3_first_name': 'Passenger 3 First Name',
            'passenger3_last_name': 'Passenger 3 Last Name',
            'passenger4_first_name': 'Passenger 4 First Name',
            'passenger4_last_name': 'Passenger 4 Last Name',

        }



        