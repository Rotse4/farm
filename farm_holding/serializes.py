from rest_framework import serializers
from .models import FarmHoldings

class FarmHoldingsSerializer(serializers.ModelSerializer):
    class Meta:
        model=FarmHoldings
        fields=["name",'acrage','areaunit','landsize','lat','long','accuracy', 'legstatus', 'other_farms']

