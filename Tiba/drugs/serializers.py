from rest_framework import serializers
from drugs.models import Drugs, Prescription

class DrugsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drugs
        fields = ('id', 'name', 'medicine_type', 'unit', 'unit_remaining')

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ('id', 'drug_id','consultation_id')
        