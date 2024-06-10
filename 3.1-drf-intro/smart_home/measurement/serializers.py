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
        # fields = ['temperature', 'created_at', 'sensor']
        # read_only_fields = ['sensor']

    # def create(self, validated_data):
        #return Measurement.objects.create(**validated_data)


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
        # exclude = ['sensor']
        # depth = 1


class MeasurementSerializer(serializers.Serializer):
    sensor_id = serializers.IntegerField()
    temperature = serializers.FloatField()
    created_at = serializers.DateTimeField(required=False)
    # sensor = SensorSerializer(read_only=True)

    # class Meta:
    #     model = Measurement
    #     fields = ['temperature', 'created_at']
    #     fields = ['sensor', 'temperature', 'created_at']


    def create(self, validated_data):
        # return super().create(validated_data)
        return Measurement.objects.create(**validated_data)