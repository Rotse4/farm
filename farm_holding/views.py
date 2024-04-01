from django.shortcuts import render
from . models import FarmHoldings
from rest_framework.decorators import api_view
from . serializes import FarmHoldingsSerializer
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