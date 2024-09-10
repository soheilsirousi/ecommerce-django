from django.contrib import admin

from cart.models import *


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_paid')
    inlines = (CartItemInline, )