from django.urls import path

from . import views

app_name = 'evaluacion'

urlpatterns = [
    path('', views.index, name='index'),
]
