from django.urls import path
from . import views

urlpatterns = [
    path('', views.serve_react_app, name='serve_react_app'),
    path('measurements/', views.MeasurementView.as_view(), name='measurement-list'),
]
