from django.db import models
from datetime import date


CHOICES=(
    ('Single', 'Single'),
    ('Maried', 'Maried'),
)
SEX_CHOICES=(
    ('Male', 'Male'),
    ('Female', 'Female'),
)

# Create your models here.
class EnumarationGeography(models.Model):
    farmer=models.ForeignKey('IndividualDetails', on_delete=models.CASCADE, null=True)
    county=models.CharField(max_length=100)
    constituency=models.CharField(max_length=100)
    sub_county=models.CharField(max_length=100)
    ward=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    sub_location=models.CharField(max_length=100)
    village_unit_name=models.CharField(max_length=100)
    enumaration_area_no=models.CharField(max_length=100)
    shopping_center=models.CharField(max_length=100)


    def __str__(self):
        return self.county
    

class IndividualDetails(models.Model):
    farmer_name =models.CharField(max_length=100)
    national_id =models.BigIntegerField()
    email =models.CharField(max_length=100)
    date_of_birth = models.DateField(null =True)
    postal=models.CharField(max_length=100)
    postal_code=models.IntegerField()
    mobile_number=models.CharField(max_length=100)
    marital_status=models.CharField(choices=CHOICES, max_length=100, default='Single')
    sex=models.CharField(choices=SEX_CHOICES, max_length=100)
    hh_size=models.IntegerField()
    training=models.BooleanField()

    def __str__(self):
        return self.farmer_name
