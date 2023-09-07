from django.contrib import admin

from .models import *

class RealEstateAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'purchased')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = ('purchased',)
    list_filter = ('purchased', 'time_create')

class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')
    list_display_links = ('id', 'type')
    search_fields = ('type',)


admin.site.register(RealEstate, RealEstateAdmin)
admin.site.register(PropertyType, PropertyTypeAdmin)
