from django.db import models
from farmer_identification.models import IndividualDetails

# Create your models here.
class FarmHoldings(models.Model):
    farmer=models.ForeignKey(IndividualDetails, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=100)
    acrage=models.IntegerField()
    areaunit=models.CharField(max_length=50)
    landsize=models.IntegerField()
    lat=models.DecimalField(decimal_places=5,max_digits=10, null=True)
    long=models.DecimalField(decimal_places=5,max_digits=10, null=True)
    accuracy=models.IntegerField()
    legstatus=models.CharField(max_length=100)
    other_farms=models.BooleanField()

    def __str__(self):
        return self.name
    

class Crop(models.Model):
    farmer=models.ForeignKey(IndividualDetails, on_delete=models.CASCADE, null=True)
    crop=models.CharField(max_length=100)
    total_acrage=models.IntegerField()
    unit_area=models.CharField(max_length=100)
    certified_seeds=models.CharField(max_length=100)
    purpose=models.CharField(max_length=100)
    water_source=models.CharField(max_length=50)
    crop_system=models.CharField(max_length=100)
    fertilizer=models.CharField(max_length=100)
    pestcide=models.CharField(max_length=100)


    def __str__(self):
        return self.crop
    
