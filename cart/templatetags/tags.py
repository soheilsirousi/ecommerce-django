from django import template

register = template.Library()


@register.simple_tag()
def cart_items(request):
    cart = request.user.carts.last()
    if cart:
        return cart.items