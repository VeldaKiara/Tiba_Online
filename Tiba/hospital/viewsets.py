from rest_framework import viewsets
from .models import Hospital, User_Hospital
from .serializers import HospitalSerializer, User_HospitalSerializer

class HospitalViewSets(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class User_HospitalViewSets(viewsets.ModelViewSet):
    queryset = User_Hospital.objects.all()
    serializer_class = User_HospitalSerializer
    