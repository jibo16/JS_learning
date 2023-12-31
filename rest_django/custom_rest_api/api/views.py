from django.shortcuts import render
from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    data["headers"] = dict(request.headers)
    print(data)
    return JsonResponse(data)

