from django.contrib import admin
from . models import EnumarationGeography, IndividualDetails

class IndividualDetailsAdmin(admin.ModelAdmin):
    model = IndividualDetails
    list_display = ('farmer_name', 'national_id', 'email', 'date_of_birth', 'postal', 'mobile_number', 'sex', 'hh_size', 'training')


admin.site.register(IndividualDetails, IndividualDetailsAdmin)