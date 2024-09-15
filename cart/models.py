from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from store.models import Product
from utils.models import AbstractModel

class Cart(AbstractModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='carts', verbose_name=_('user'))
    is_paid = models.BooleanField(default=False, verbose_name=_('is paid'))

    class Meta:
        verbose_name = _('cart')
        verbose_name_plural = _('carts')


class CartItem(AbstractModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', verbose_name=_('cart'))
    item = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='carts', verbose_name=_('item'))
    quantity = models.PositiveSmallIntegerField(default=1, verbose_name=_('quantity'))

    class Meta:
        verbose_name = _('cart item')
        verbose_name_plural = _('cart items')