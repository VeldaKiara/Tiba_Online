from django.db import models
from accounts.models import *
# Create your models here.

class Consultation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    symptoms = models.CharField(max_length=1000)
    temparature = models.IntegerField(blank=False, null=False)
    blood_pressure = models.IntegerField(blank=False, null=False)
    diagnosis = models.CharField(max_length=1000)
    doctor_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='doctor')
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='patient')
    class Meta:
        pass

class Reffer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hospital = models.CharField(max_length=300)
    note_to_specialist = models.CharField(max_length=300)
    current_prescriptions = models.CharField(max_length=300)
    class Meta:
        pass

class Admit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ward = models.CharField(max_length=300)
    specialist = models.CharField(max_length=300)
    note_to_specialist = models.CharField(max_length=300)
    current_prescriptions = models.CharField(max_length=300)
    class Meta:
        pass

    


    
    