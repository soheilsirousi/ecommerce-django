from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=11, unique=True, null=False, blank=False, verbose_name=_("phone"))
    national_id = models.CharField(max_length=10, unique=True, null=True, blank=True, verbose_name=_("national id"))
    country = models.CharField(max_length=30, blank=True, null=True, verbose_name=_("country"))

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ('username', 'password')

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.username