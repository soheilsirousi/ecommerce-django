from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.models import AbstractModel

class Category(AbstractModel):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='categories')
    name = models.CharField(_('name'), max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")


class Product(AbstractModel):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False, verbose_name=_('product'))
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=False, blank=False, related_name='products')
    price = models.PositiveBigIntegerField(verbose_name=_('price'), null=False, blank=False)
    info = models.TextField(verbose_name=_('info'), null=False, blank=False)

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")


class ProductImage(AbstractModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False, related_name='images')
    image = models.ImageField(upload_to="products", null=False, blank=False, verbose_name=_("image"))

    class Meta:
        verbose_name = _("product image")
        verbose_name_plural = _("product images")


class ProductAttribute(AbstractModel):
    name = models.CharField(verbose_name=_('name'), max_length=100, null=False, blank=False)

    class Meta:
        verbose_name = _("product attribute")
        verbose_name_plural = _("product attributes")


class ProductAttributeValue(AbstractModel):
    attribute = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE, null=False, blank=False, related_name='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False, related_name='attributes')
    value = models.CharField(max_length=100, null=False, blank=False, verbose_name=_('value'))

    class Meta:
        verbose_name = _('product attribute value')
        verbose_name_plural = _('product attributes values')


class Comment(AbstractModel):
    reply_to = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies', verbose_name=_('reply to'))
    message = models.TextField(verbose_name=_('message'))

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')

    def __str__(self):
        return self.message
