from django.shortcuts import render
import django_filters
import json
from rest_framework import viewsets, filters
from django.http import HttpResponse
import api.search as search
from .models import restaurant

def apiview(request):
    lat = request.GET['lat'] #緯度
    lng = request.GET['lng'] #経度

    currentPosition = {"lat":float(lat),"lng":float(lng)}

    obj = []

    for i in restaurant.objects.all():
        restaurantPosition = {"lat":float(i.lat),"lng":float(i.lng)}
        dist = search.dist_on_sphere(currentPosition,restaurantPosition)
        if dist <= 5:
            obj.append({"name":i.name,"description":i.description,"address":i.address,"image":i.url})

    json_str = json.dumps(obj, ensure_ascii=False, indent=2)

    return HttpResponse(json_str, content_type='application/json; charset=UTF-8')


