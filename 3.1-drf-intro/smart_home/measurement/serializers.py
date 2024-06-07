from rest_framework import serializers
from measurement.models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['name', 'description'] #'__all__'


class MeasurementSerializer(serializers.ModelSerializer):

    # def create(self, validated_data):
    #     return super().create(validated_data)
        #return Measurement.objects.create(**validated_data)

    class Meta:
        model = Measurement
        # fields = ['temperature', 'created_at']
        fields = ['temperature', 'created_at', 'sensor']
        # read_only_fields = ['sensor']

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
        # exclude = ['sensor']
        # depth = 1