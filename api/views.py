from django.shortcuts import render
from django.http import JsonResponse
from .models import itemModel
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def modelView(request):

    if request.method == 'GET':
        data = serializers.serialize('json', itemModel.objects.all())
        return JsonResponse(json.loads(data), safe=False)
    
    if request.method == 'POST':
        body = json.loads( request.body.decode('utf-8'))
        newrecord = itemModel.objects.create(
            item=body['item'],
            featured=body['featured'],
            price=body['price'])
        data = json.loads(serializers.serialize('json', [newrecord]))
        return JsonResponse(data, safe=False)
    
@csrf_exempt
def modelView2(request, id):

    if (request.method == "PUT"):
    # Turn the body into a dict
        body = json.loads(request.body.decode("utf-8"))
    # update the item
        itemModel.objects.filter(pk=id).update(
            item=body['item'],
            featured=body['featured'],
            price=body['price'])
        newrecord = itemModel.objects.filter(pk=id)
    # Turn the object to json to dict, put in array to avoid non-iterable error
        data = json.loads(serializers.serialize('json', newrecord))
    # send json response with updated object
        return JsonResponse(data, safe=False)

    if (request.method == "DELETE"):
    # delete the item, get all remaining records for response
        itemModel.objects.filter(pk=id).delete()
        newrecord = itemModel.objects.all()
    # Turn the results to json to dict, put in array to avoid non-iterable error
        data = json.loads(serializers.serialize('json', newrecord))
    # send json response with updated object
        return JsonResponse(data, safe=False)

    


