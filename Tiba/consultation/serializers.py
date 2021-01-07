from rest_framework import serializers
from consultation.models import Consultation, Reffer, Admit

class ConsultationSerializer(serializers.ModelSerializer):
    	class Meta:
		model = Consultation
		fields=('id','','symptoms','temparature','blood_pressure_a','blood_pressure_b','diagnosis','doctor_id','user_id')
  
class RefferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reffer
        fields = ('id', 'hospital','note_to_specialist','current_prescriptions')
        
class AdmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admit
        fields = ('id', 'ward', 'specialist', 'note_to_specialist', 'current_prescriptions')