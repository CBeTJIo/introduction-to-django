from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, CreateAPIView
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreate(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    # def post(self, request, *args, **kwargs):
    #     new_sensor = Sensor.objects.create(
    #         name=request.data['name'],
    #         description=request.data['description']
    #     )
    #     return self.create(request, new_sensor)

    # def patch(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk', None)
    #     instance = Sensor.objects.get(pk=pk)
    #     print(pk)
    #     print(instance)
    #     serializer = SensorSerializer(data=request.data, instance=instance)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response('Изменения внесены')