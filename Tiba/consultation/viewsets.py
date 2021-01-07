from rest_framework import viewsets
from .models import Consultation, Reffer, Admit
from .serializers import ConsultationSerializer, RefferSerializer, AdmitSerializer

class ConsultationViewSets(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    
class RefferViewSets(viewsets.ModelViewSet):
    queryset = Reffer.objects.all()
    serializer_class = RefferSerializer
    
class AdmitViewSets(viewsets.ModelViewSet):
    queryset = Admit.objects.all()
    serializer_class = AdmitSerializer
    
  