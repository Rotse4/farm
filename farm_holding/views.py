from django.shortcuts import render
from . models import FarmHoldings,Crop
from rest_framework.decorators import api_view
from . serializes import FarmHoldingsSerializer,CropSerializer
from rest_framework.response import Response


# Create your views here.

@api_view(['POST'])
def post_farm_holdings(request):
    holdings = request.data
    serializer=FarmHoldingsSerializer(data=holdings)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors)


@api_view(['POST'])
def crop(request):
    serializer=CropSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors) 

@api_view(['GET'])
def get_crop(request):
    location= Crop.objects.all()
    serilizer= CropSerializer(location, many=True)
    return Response({'crops': serilizer.data})

@api_view(['GET'])
def get_farm_holdings(request):
    farms= FarmHoldings.objects.all()
    serilizer= FarmHoldingsSerializer(farms, many=True)
    return Response({'farm': serilizer.data})

