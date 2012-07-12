# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from mptt.managers import TreeManager
from shop_categories.models.defaults.category.base import ProductCategoryBase

class Category(ProductCategoryBase):
    tree = TreeManager()
    
    class Meta:
        abstract = False
        app_label = 'shop_categories'
        verbose_name = _('Product Category')
        verbose_name_plural = _('Product Categorys')  