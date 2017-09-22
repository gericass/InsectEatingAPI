from django.shortcuts import render
import django_filters

from rest_framework import viewsets, filters
from django.http import HttpResponse
from .models import restaurant



def apiview(request):
    lat = request.GET['lat'] #緯度
    lng = request.GET['lng'] #経度




    return HttpResponse(lat+lng)


