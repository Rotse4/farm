from django.contrib import admin
from . models import FarmHoldings, Crop

# Register your models here.
class CropAdmin(admin.ModelAdmin):
    model = Crop
    list_display = ('farmer', 'crop', 'total_acrage', 'certified_seeds', 'water_source', 'crop_system', 'fertilizer', 'pestcide')


admin.site.register(Crop, CropAdmin)