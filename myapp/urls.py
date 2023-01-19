from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_code, name='generate_code'),
]
