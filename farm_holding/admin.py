from django.contrib import admin
from . models import FarmHoldings, Crop

# Register your models here.
class CropAdmin(admin.ModelAdmin):
    model = Crop
    list_display = ('farmer', 'crop', 'total_acrage', 'certified_seeds', 'water_source', 'crop_system', 'fertilizer', 'pestcide')


class FarmHoldingsAdmin(admin.ModelAdmin):
    model = FarmHoldings
    list_display = ('farmer', 'name', 'acrage', 'areaunit', 'landsize', 'lat', 'long', 'accuracy','legstatus','other_farms')




admin.site.register(Crop, CropAdmin)
admin.site.register(FarmHoldings, FarmHoldingsAdmin)