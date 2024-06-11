from rest_framework import serializers
from measurement.models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description'] #'__all__'


class MeasurementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementDetailSerializer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature']
    # sensor_id = serializers.IntegerField()
    # temperature = serializers.FloatField()
    # created_at = serializers.DateTimeField(required=False)
    #
    # def create(self, validated_data):
    #     return Measurement.objects.create(**validated_data)



    # fields = ['temperature', 'created_at']
    # fields = ['sensor', 'temperature', 'created_at']

        # fields = ['temperature', 'created_at', 'sensor']
        # read_only_fields = ['sensor']

    # def create(self, validated_data):
        #return Measurement.objects.create(**validated_data)


        # exclude = ['sensor']
        # depth = 1