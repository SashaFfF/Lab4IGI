from django.contrib import admin

from .models import *

class RealEstateAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'purchased')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = ('purchased',)
    list_filter = ('purchased', 'time_create')
    prepopulated_fields = {"slug": ("title",)}

class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')
    list_display_links = ('id', 'type')
    search_fields = ('type',)
    prepopulated_fields = {"slug": ("type",)}

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number')
    list_display_links = ('id', 'last_name')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number', 'position')
    list_display_links = ('id', 'last_name', 'position')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number')
    list_display_links = ('id', 'last_name')

class DealAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'buyer', 'agent')
    list_display_links = ('id',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'answer', 'date')


class PromotionalCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_date', 'end_date')
    list_display_links = ('id', 'end_date')


class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_vacant')
    list_display_links = ('id', 'name')

admin.site.register(RealEstate, RealEstateAdmin)
admin.site.register(PropertyType, PropertyTypeAdmin)
admin.site.register(ServiceType)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Deal, DealAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(PromotionalCode, PromotionalCodeAdmin)
admin.site.register(Position, PositionAdmin)
