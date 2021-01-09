from rest_framework import serializers
from hospital.models import Hospital, User_Hospital

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ('id', 'name', 'sub_county', 'hospital_level', 'is_referral')

class User_HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Hospital
        fields = ('id', 'user_id', 'hospital_id')
