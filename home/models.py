# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Shelfs(models.Model):

    #__Shelfs_FIELDS__
    shelfbarcode = models.CharField(max_length=255, null=True, blank=True)

    #__Shelfs_FIELDS__END

    class Meta:
        verbose_name        = _("Shelfs")
        verbose_name_plural = _("Shelfs")


class Products(models.Model):

    #__Products_FIELDS__
    productname = models.CharField(max_length=255, null=True, blank=True)

    #__Products_FIELDS__END

    class Meta:
        verbose_name        = _("Products")
        verbose_name_plural = _("Products")


class Inventory(models.Model):

    #__Inventory_FIELDS__
    productfk = models.ForeignKey(Products, on_delete=models.CASCADE)
    shelffk = models.ForeignKey(Shelfs, on_delete=models.CASCADE)
    qty = models.IntegerField(null=True, blank=True)

    #__Inventory_FIELDS__END

    class Meta:
        verbose_name        = _("Inventory")
        verbose_name_plural = _("Inventory")



#__MODELS__END
