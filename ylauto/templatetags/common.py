from django import template
from product.models import Category

register = template.Library()

@register.simple_tag
def get_category_icon(request, cat_id):
    if cat_id == 1:
        return 'icon-eu'
    if cat_id == 2:
        return 'icon-am'
    if cat_id == 3:
        return 'icon-jp'
    if cat_id == 6:
        return 'icon-else'

@register.assignment_tag
def get_categories():
    cats = Category.objects.all()
    return cats

