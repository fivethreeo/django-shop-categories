# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from shop_categories.models.defaults.product.base import CategoryProductBase
        
class CategoryProduct(CategoryProductBase):     
    
    class Meta:
        abstract = False
        app_label = 'shop_categories'
        verbose_name = _('Category Product')
        verbose_name_plural = _('Category Products')        
        