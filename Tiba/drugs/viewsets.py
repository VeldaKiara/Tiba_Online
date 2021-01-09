from rest_framework import viewsets
from .models import Drugs, Prescription
from .serializers import DrugsSerializer, PrescriptionSerializer

class DrugsViewSets(viewsets.ModelViewSet):
    queryset = Drugs.objects.all()
    serializer_class = DrugsSerializer

class PrescriptionViewSets(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    
    
