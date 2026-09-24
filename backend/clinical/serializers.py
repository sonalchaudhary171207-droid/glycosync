from rest_framework import serializers
from .models import GlucoseReading, SafetyRule


class GlucoseReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlucoseReading
        fields = '__all__'


class SafetyRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SafetyRule
        fields = '__all__'