from django import template

from store.models import Category

register = template.Library()

@register.simple_tag(name='categories')
def categories():
    return Category.objects.all()