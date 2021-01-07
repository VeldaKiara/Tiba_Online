from rest_framework import serializers
from consultation.models import Consultation, Reffer, Admit

class ConsultationSerializer(serializers.ModelSerializer):
    	class Meta:
		model = Consultation
		fields=('id','condition','user_id')