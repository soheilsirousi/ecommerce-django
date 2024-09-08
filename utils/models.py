from django.db import models
from django.utils.translation import gettext_lazy as _

class AbstractModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=_("created time"))
    modified_time = models.DateTimeField(auto_now=True, verbose_name=_("modified time"))

    class Meta:
        abstract = True