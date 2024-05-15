from django.urls import path

from calculator.views import food_view

urlpatterns = [
    path('<food>/', food_view, name='food')
]
