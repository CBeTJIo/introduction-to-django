from django.urls import path
from measurement.views import SensorView, SensorUpdate, MeasurementsCreate

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorUpdate.as_view()),
    path('measurements/', MeasurementsCreate.as_view()),
]