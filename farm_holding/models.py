from django.db import models

# Create your models here.
class FarmHoldings(models.Model):
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


