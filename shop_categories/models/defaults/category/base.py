from django.db import models
from django.utils.encoding import force_unicode
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey

class ProductCategoryBase(MPTTModel):
    
    parent = TreeForeignKey('self', 
        blank=True, 
        null=True, 
        related_name="children", 
        verbose_name='Parent')    
        
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    
    path = models.CharField(max_length=255)
    name_path = models.CharField(max_length=255)

    active = models.BooleanField()
    
    class Meta:
        abstract = True
    
    def __unicode__(self):
        return self.name_path
        
    def short_title(self):
        return self.name
        
    def get_path(self):
        ancestors = []
        if self.parent:
            ancestors = list(self.parent.get_ancestors(include_self=True))
        ancestors = ancestors + [self,]
        return ancestors
        
    def join_path(self, joiner, field, ancestors):
        return joiner.join([force_unicode(getattr(i, field)) for i in ancestors])
        
    def save(self, *args, **kwargs):
        
        ancestors = self.get_path()
        self.path = self.join_path(u'/', 'slug', ancestors)
        self.name_path =  self.join_path(u'> ', 'name', ancestors)
        
        update_descendants = bool(self.pk)
        super(ProductCategoryBase, self).save(*args, **kwargs)
        
        if update_descendants:
            children = list(self.children.all())
            for child in children:
                child.active = self.active
                child.save()
                
    @models.permalink    
    def get_absolute_url(self):
        return('product_list', (), {'path': self.path})            