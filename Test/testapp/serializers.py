from rest_framework import serializers
from .models import Period, User



class PeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Period
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    period = PeriodSerializer(many=True)
    class Meta:
        model = User
        fields = "__all__"
        depth = 1

    