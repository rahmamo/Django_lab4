from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from rest_framework.response import Response
from rest_framework import status
from .serlializers import *


@api_view(['GET'])
def list(request,id=0):
    if id==0 :
          trainess=Trainee.objects.all()
          if trainess :
                 data = Traineeserilzer(trainess, many=True)
                 #many :return more than one
                 print(data.data)
                 return Response(data.data)
          else:
              return Response("data is empty")
    else:
        trainess = Trainee.objects.get(id=id)
        if trainess:
              data=Traineeserilzer(trainess)
              # many :not use many because return one
              return Response(data.data)
        else:
            return Response({'error': 'trainee not found'})



@api_view(['POST'])
def insert(request):
    print(request.data)
    t=Traineeserilzer(data=request.data)
    if t.is_valid():
        t.save()
        return Response(t.data)
    else:
        return Response(status=status.HTTP_306_RESERVED)

@api_view(['PUT'])
def update(request,id):
    trainess = Trainee.objects.get(id=id)
    data = Traineeserilzer(instance=trainess, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_306_RESERVED)


@api_view(['DELETE'])
def delete(request,id):
    trainess = Trainee.objects.get(id=id)
    trainess.delete()
    return Response("done")

