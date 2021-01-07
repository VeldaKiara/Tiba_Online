from rest_framework import viewsets
from .models import Conditions, CustomUser
from .serializers import ConditionsSerializer, CustomUserSerializer

class ConditionsViewSets(viewsets.ModelViewSet):
    queryset = Conditions.objects.all()
    serializer_class = ConditionsSerializer
    
class CustomUserViewSets(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
    
