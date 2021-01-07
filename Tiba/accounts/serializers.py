from rest_framework import serializers
from accounts.models import Conditions, CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'user_type', 'gender', 'specialization', 'license_number', 'profession','date_of_birth','id_number', 'residence')

class ConditionsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Conditions
		fields=('id','condition','user_id')