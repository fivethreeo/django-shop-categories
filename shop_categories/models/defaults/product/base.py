from django.db import models
from shop.models.defaults.bases import BaseProduct
from mptt.fields import TreeForeignKey, TreeManyToManyField
from shop_categories.utils import get_category_model_string

class CategoryProductBase(BaseProduct):
    main_category = TreeForeignKey(get_category_model_string('Category'))
    additional_categories = TreeManyToManyField(get_category_model_string('Category'), related_name='extra_product_categories')

    class Meta:
        abstract = True
        
    @models.permalink    
    def get_absolute_url(self):
        return('product_detail', (), {'slug':self.slug, 'path': self.main_category.path})
        
    def save(self, *args, **kwargs):
        super(CategoryProductBase, self).save(*args, **kwargs)
        self.additional_categories.add(self.main_category)

