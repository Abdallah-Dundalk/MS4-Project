from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import datetime
# Create your models here.

ON_SITE_STATUS = ((0, "On Site"), (1, "Off Site"))

OVER_STAYED_STATUS = ((0, "OK"), (1, "Over Stayed"))


class AccessLog(models.Model):
    gate_number = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    passenger1_first_name = models.CharField(max_length=50, default="", blank=True, null=True)
    passenger1_last_name = models.CharField(max_length=50, default="", blank=True, null=True)
    passenger2_first_name = models.CharField(max_length=50, default="", blank=True, null=True)
    passenger2_last_name = models.CharField(max_length=50, default="", blank=True, null=True)
    passenger3_first_name = models.CharField(max_length=50, default="", blank=True, null=True)
    passenger3_last_name = models.CharField(max_length=50, default="", blank=True, null=True)
    passenger4_first_name = models.CharField(max_length=50, default="", blank=True, null=True)
    passenger4_last_name = models.CharField(max_length=50, default="", blank=True, null=True)
    phone_number = models.IntegerField()
    registration = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    time_in = models.TimeField()
    time_out = models.TimeField(null=True, blank=True)
    entry_date = models.DateField()
    exit_date = models.DateField(null=True, blank=True)
    on_site_status = models.BooleanField(default=True, null=True)
    over_stayed_status = models.BooleanField(default=False, null=True)
    signature = models.CharField(max_length=10000)
    parking_time_limit = models.TimeField()
    officers_name = models.CharField(max_length=50, default="")
    created_on = models.DateTimeField()
   
    


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.company

    
