from django.urls import path
from measurement.views import SensorView, SensorUpdate, MeasurementCreate

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorUpdate.as_view()),
    path('measurements/', MeasurementCreate.as_view()),
]