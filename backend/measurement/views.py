from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Measurement
from .serializers import MeasurementSerializer
import json
from decimal import Decimal
from django.shortcuts import render

def serve_react_app(request):
    return render(request, 'index.html')

def filter_database(height, age, weight, data, tolerance=2):
    filtered_data = []
    for entry in data:
        height_diff = abs(Decimal(height) - entry.height)
        age_diff = abs(Decimal(age) - entry.age)
        weight_diff = abs(Decimal(weight) - entry.weight)

        if height_diff <= tolerance and age_diff <= tolerance and weight_diff <= tolerance:
            filtered_data.append(entry)
    return filtered_data

class MeasurementView(APIView):
    def get(self, request, format=None):
        height = float(request.query_params.get('height'))
        age = float(request.query_params.get('age'))
        weight = float(request.query_params.get('weight'))

        data = Measurement.objects.all()
        filtered_data = filter_database(height, age, weight, data)
        waist_ranges = [entry.waist for entry in filtered_data]
        return Response(waist_ranges)

    def post(self, request, format=None):
        data = request.data

        height = float(data.get('height'))
        weight = float(data.get('weight'))
        age = float(data.get('age'))
        waist = float(data.get('waist'))

        existing_record = Measurement.objects.filter(height=height, weight=weight, age=age, waist=waist)

        if existing_record.exists():
            return JsonResponse({'status': 'ALREADY_PRESENT'})
        else:
            new_measurement = Measurement(height=height, weight=weight, age=age, waist=waist)
            new_measurement.save()
            return JsonResponse({'status': 'SUCCESS'})
