from django.shortcuts import render
from django.http import HttpRequest ,HttpResponse
import requests
import json


def callgetmethod(request):
    url="http://127.0.0.1:8000/trainee/list/"
    head = {'contnet-type': 'application/json'}
    res = requests.get(url=url, headers=head)
    print(res.json())
    return HttpResponse("get")

def callpostmethod(request):
    url = "http://127.0.0.1:8000/trainee/insert/"
    header = {
        "Content-Type": "application/json",
    }
    data = {
        "name": "rahma",
        "nationalnumber": "12563984",
        "courses" : "1",
    }
    result = requests.post(url=url, data=json.dumps(data), headers=header)
    if result.status_code == 200:
        return HttpResponse('Successful Inserted')
    return HttpResponse('Something went wrong')
