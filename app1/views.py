from distutils.log import error
from gzip import READ
from turtle import st
from django.shortcuts import render
from app1.serializers import SpaceDbSerializer
from app1.models import SpaceDb
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])
def display(request):
    if request.method == 'GET':
        modeldb = SpaceDb.objects.all()
        serializerdb = SpaceDbSerializer(modeldb, many = True)
        return Response(serializerdb.data,status=status.HTTP_202_ACCEPTED)

    # return Response(serializerdb.data,status=status.HTTP_202_ACCEPTED)

    elif request.method == 'POST':
        modeldb = SpaceDb.objects.all()
        serializerdb = SpaceDbSerializer(data = request.data)
        if serializerdb.is_valid():
            serializerdb.save()
            return Response(serializerdb.data, status= status.HTTP_201_CREATED)
        
        return Response(serializerdb.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','PATCH','DELETE'])    
def edit(request, pk):
    try:
        transformer = SpaceDb.objects.get(pk=pk)
    except SpaceDb.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
  
    if request.method == 'GET':
        serializer = SpaceDbSerializer(transformer)
        return Response(serializer.data)
  
    elif request.method == 'PUT':
        serializer = SpaceDbSerializer(transformer, data=request.data)
  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'PATCH':
        serializer = SpaceDbSerializer(transformer,data=request.data,partial=True)
  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
    elif request.method == 'DELETE':
        transformer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








