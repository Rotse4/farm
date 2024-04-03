from rest_framework import serializers
from .models import FarmHoldings,Crop

class FarmHoldingsSerializer(serializers.ModelSerializer):
    class Meta:
        model=FarmHoldings
        fields=["name",'acrage','areaunit','landsize','lat','long','accuracy', 'legstatus', 'other_farms']


class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model=Crop
        fields=["farmer",'crop','total_acrage','certified_seeds','purpose','water_source','crop_system', 'fertilizer', 'pestcide']


