from django.db import models
import uuid
from accounts.models import *
# Create your models here.

HOSPITAL_LEVELS=[
    ('1','Community Facilities, Level 1'),
    ('2','Health Dispensaries, Level 2'),
    ('3','Health Centres, Level 3'),
    ('4','County Hospitals, Level 4'),
    ('5','County Referral Hospitals, Level 5'),
    ('6','National Referral Hospitals, Level 6'),
]
BOOL_CHOICES = [ 
    (True, 'Yes'), 
    (False, 'No'),
]

class Hospital(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    sub_county = models.CharField(max_length=250)
    hospital_level = models.CharField(choices=HOSPITAL_LEVELS, default=1,  max_length=250)
    is_referral = models.BooleanField(default=False, choices=BOOL_CHOICES, max_length=25)
    class Meta:
        pass

class User_Hospital(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    hospital_id = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    class Meta:
        pass

    
    
    
    
    
    

    