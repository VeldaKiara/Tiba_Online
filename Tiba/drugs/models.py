from django.db import models
from consultation.models import * 
# Create your models here.

class Drugs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1000, null=False, blank=False)
    medicine_type = models.CharField(max_length=240, null=False, blank=False)
    unit = models.IntegerField(default=0)
    unit_remaining = models.IntegerField(default=0)
    class Meta:
        pass

class Prescription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    drug_id = models.ForeignKey(Drugs, on_delete=models.CASCADE)
    consultation_id = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    class Meta:
        pass

    