from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def MyfirstView(request):

    date = {
        'nombre': 'Joel German'
    }
    return JsonResponse(date)