from rest_framework import viewsets
from .models import Conditions, CustomUser
from .serializers import ConditionsSerializer, CustomUserSerializer

class ConditionsViewSets(viewsets.ModelViewSet):
    queryset = Conditions.objects.all()
    serializer_class = ConditionsSerializer
    
class CustomUserSerializer(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
    
