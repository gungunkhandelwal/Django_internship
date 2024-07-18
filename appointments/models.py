from django.db import models
from django.conf import settings
import datetime
from datetime import date,timedelta,datetime

class Appointments(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appointments_as_patient')
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appointments_as_doctor')
    speciality = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def save(self,*args,**kwargs):
        if not self.end_time:
            self.end_time = (datetime.combine(date.today(), self.start_time) + timedelta(minutes=45)).time()
        super().save(*args, **kwargs)
