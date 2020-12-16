from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

USER_TYPES = [
    (0, 'Doctor'),
    (1, 'Pharmacist'),
    (2,'Patient'),
]
GENDER_CHOICES=[
    (0, 'Female'),
    (1, 'Male'),
    (2,'Lesbian'),
    (3,'Gay'),
    (4,'Bisexual'),
    (5,'Transgender'),
    (6,'Queer'),
]



class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_type = models.IntegerField(choices=USER_TYPES)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    specialization = models.CharField( max_length=250,null=True, blank=True)
    license_number = models.CharField(max_length=250, null=True, blank=True)
    profession = models.CharField(max_length=250, null=True, blank=True)
    date_of_birth = models.CharField(max_length=250, null=False, blank=False)
    id_number = models.CharField(max_length=250,null=True, blank=True)
    residence = models.CharField( max_length=250, null=False, blank=False)
    class Meta:
        pass
    def __str__(self):
        return self.username
    
class Conditions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    condition = models.CharField(max_length=1000, null=True, blank=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    class Meta:
        pass
    


    

