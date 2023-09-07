from django import template
from real_estate.models import *

register = template.Library()

@register.simple_tag(name='gettypes')
def get_types(filter=None):
    if not filter:
        return PropertyType.objects.all()
    else:
        return PropertyType.objects.filter(pk=filter)

@register.inclusion_tag('real_estate/list_types.html')
def show_types(sort=None, type_selected=0):
    if not sort:
        types = PropertyType.objects.all()
    else:
        types = PropertyType.objects.order_by(sort)
    return {"types": types, "type_selected": type_selected}
