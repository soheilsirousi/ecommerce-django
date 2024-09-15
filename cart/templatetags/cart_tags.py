from django import template

register = template.Library()


@register.simple_tag(name='cart_items', takes_context=True)
def cart_items(context):
    if not context['request'].user.is_authenticated:
        return None
    cart = context['request'].user.carts.last()
    if cart:
        return cart.items.all()


@register.simple_tag(name='cart_total', takes_context=True)
def cart_total(context):
    if not context['request'].user.is_authenticated:
        return None
    price = 0
    cart = context['request'].user.carts.last()
    if cart:
        for item in cart.items.all().iterator():
            price = price + (item.item.price * item.quantity)
        return price