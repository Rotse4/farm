from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializers import IndividualDetailSerializer, EnumarationSerializer
from . models import IndividualDetails

# Create your views here.



@api_view(['POST'])
def register(request):
    serializer= IndividualDetailSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors)

@api_view(['POST'])
def geography(request):
    serializer= EnumarationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors)

@api_view(['POST'])
def compined(request):
    serializer= IndividualDetailSerializer(data=request.data)
    geo_serializer= EnumarationSerializer(data=request.data)
    if serializer.is_valid():
        if geo_serializer.is_valid():
            geo_serializer.save()
            
            serializer.save()
            print("okkk")
            return Response({"user_data":serializer.data, "geo_data":geo_serializer.data},)
        else:
            print('not okk')
    
    
    return Response(geo_serializer.errors)


@api_view(['GET'])
def get_farmers(request):
    farmers= IndividualDetails.objects.all()
    serilizer= IndividualDetailSerializer(farmers, many=True)
    return Response({'farmers': serilizer.data})




