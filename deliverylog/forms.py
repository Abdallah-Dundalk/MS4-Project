from django import forms
from .models import AccessLog

import datetime


class AccessForm(forms.ModelForm):
    class Meta:
        model = AccessLog
        fields = '__all__'
        