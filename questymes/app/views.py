from datetime import datetime
from .serializers import UserSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Slot


# Create your views here.
@api_view(['GET'])
def welcome(request):
    return Response('Welcome to the Django app')


@api_view(['POST'])
def saveSlot(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer)
        serializer.save()
    else:
        print("error")
    return Response("slot")

