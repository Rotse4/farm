from django.contrib import admin
from . models import EnumarationGeography, IndividualDetails

class IndividualDetailsAdmin(admin.ModelAdmin):
    model = IndividualDetails
    list_display = ('farmer_name', 'national_id', 'email', 'date_of_birth', 'postal', 'mobile_number', 'sex', 'hh_size', 'training')



class EnumarationGeographyAdmin(admin.ModelAdmin):
    model = EnumarationGeography
    list_display = ('farmer', 'county', 'constituency', 'sub_county', 'ward', 'sub_location', 'village_unit_name', 'enumaration_area_no', 'shopping_center')


admin.site.register(IndividualDetails, IndividualDetailsAdmin)
admin.site.register(EnumarationGeography, EnumarationGeographyAdmin)