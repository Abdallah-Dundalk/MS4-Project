from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import datetime
# Create your models here.

ON_SITE_STATUS = ((0, "On Site"), (1, "Off Site"))

OVER_STAYED_STATUS = ((0, "OK"), (1, "Over Stayed"))


class AccessLog(models.Model):
    null = True
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
    time_in = models.DateTimeField(blank=True)
    time_out = models.DateTimeField(blank=True, null=True, default=None)
    entry_date = models.DateField(auto_now_add=True)
    on_site_status = models.BooleanField(default=True, null=True)
    over_stayed_status = models.BooleanField(default=False, null=True)
    signature = CloudinaryField('image', default='placeholder', null=True)
    parking_time_limit = models.DateTimeField(blank=True)
    officers_name = models.CharField(max_length=50, default="", blank=True)
    created_on = models.DateTimeField(auto_now=True, null=True)
    


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.company

    
