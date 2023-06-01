from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer


# Create your views here.

@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print(serializer)
    return Response(serializer.data)


@api_view(['GET'])
def welcome(request):
    return Response("Welcome to Django")
