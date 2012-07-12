# -*- coding: utf-8 -*-
from decimal import Decimal
from shop.models.productmodel import Product # is the overridden CategoryProduct (project.models.product.Product)
from shop_categories.models.categorymodel import Category # is the overridden Category (project.models.category.Category)

from django.test.testcases import TestCase
from django.template.defaultfilters import slugify

def make_category_tree():
    top = Category(name='Top category', slug=slugify('Top category'), active=True)
    top.save()
    level1_first = Category(name='Level1 first', slug=slugify('Level1 first'), active=True, parent=top)
    level1_first.save()
    level1_second = Category(name='Level1 second', slug=slugify('Level1 second'), active=True, parent=top)
    level1_second.save()
    level2_first = Category(name='Level2 first', slug=slugify('Level2 first'), active=True, parent=level1_first)
    level2_first.save()
    level2_first_sub = Category(name='Level2 first sub', slug=slugify('Level2 first sub'), active=True, parent=level2_first)
    level2_first_sub.save()
    level2_second = Category(name='Level2 second', slug=slugify('Level2 second'), active=True, parent=level1_first)
    level2_second.save()
    Category.tree.rebuild()

class CategoryProductTestCase(TestCase):

    def setUp(self):
        make_category_tree()

    def test_tree_unicode(self):
        self.assertEqual(unicode(Category.objects.get(slug='level1-first')., 'Top category> Level1 first')
        
    def test_tree_save(self):
        Category.objects.get(slug='level1-first').save()
                
    def test_tree_count(self):
        self.assertEqual(Category.objects.count(), 6)
        
    def test_tree_leaf_path(self):
        self.assertEqual(Category.objects.get(slug='level2-first-sub').path, 'top-category/level1-first/level2-first/level2-first-sub')
    
    def test_tree_leaf_url(self):
        self.assertEqual(Category.objects.get(slug='level2-first-sub').get_absolute_url(), 'shop/catalog/top-category/level1-first/level2-first/level2-first-sub')