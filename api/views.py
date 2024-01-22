from django.shortcuts import render
from django.http import JsonResponse
import json 

# Create your views here.


def api_home(request ,  *args, **kwargs):
    body = request.body  # json data 
    data = {}

    try:
        data = json.loads(body)
    except:
        pass 

    print(data)
    return JsonResponse({"Message":"Hello there this the Django message response"})

 