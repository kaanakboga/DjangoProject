from django.contrib import admin
from .models import GeneralSetting, Ship

@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameter', 'updated_date', 'create_date']
    search_fields = ['name', 'description', 'parameter']

@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):
    list_display = ['name', 'ship_type', 'gt', 'fuel_type', 'emission_level', 'compliance_strategy']
    search_fields = ['name', 'ship_type', 'fuel_type']
    list_filter = ['fuel_type', 'compliance_strategy']
