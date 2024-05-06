from django.urls import path

from calculator.views import omlet, pasta, buter, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('omlet/', omlet, name='omlet'),
    path('pasta/', pasta, name='pasta'),
    path('buter/', buter, name='buter'),
]
