from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from core.erp.models import Category, Product


def MyfirstView(request):

    date = {
        'nombre': 'Joel German',
        'categoria': Category.objects.all()

    }
    return render(request, 'index.html', date)

def MySecondView(request):

    date = {
        'nombre': 'Joel German',
        'productos': Product.objects.all()

    }
    return render(request, 'second.html', date)