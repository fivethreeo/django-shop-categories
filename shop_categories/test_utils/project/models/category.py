from django.db import models
from shop_categories.models.defaults.category.base import ProductCategoryBase
        
class Category(ProductCategoryBase):
    
    order = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        abstract = False
        app_label = 'project'