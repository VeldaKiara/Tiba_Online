from rest_framework import serializers
from accounts.models import Conditions

class ConditionsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Conditions
		fields=('id','condition','user_id')