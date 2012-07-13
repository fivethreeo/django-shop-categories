# -*- coding: utf-8 -*-
import random
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

class CategoryTestCase(TestCase):

    def setUp(self):
        make_category_tree()

    def test_category_unicode(self):
        self.assertEqual(unicode(Category.objects.get(slug='level1-first')), 'Top category> Level1 first')
        
    def test_category_short_title(self):
        self.assertEqual(Category.objects.get(slug='level1-first').short_title(), 'Level1 first')
        
    def test_category_save(self):
        Category.objects.get(slug='level1-first').save()
                
    def test_category_count(self):
        self.assertEqual(Category.objects.count(), 6)
        
    def test_category_leaf_path(self):
        self.assertEqual(Category.objects.get(slug='level2-first-sub').path, 'top-category/level1-first/level2-first/level2-first-sub')
    
    def test_category_leaf_url(self):
        self.assertEqual(Category.objects.get(slug='level2-first-sub').get_absolute_url(), '/shop/catalog/top-category/level1-first/level2-first/level2-first-sub/')
        
class CategoryProductTestCase(TestCase):

    def setUp(self):
        make_category_tree()
        Product(
            name='Product 1',
            slug=slugify('Product 1'),
            active=True,
            unit_price=Decimal(random.randint(50, 1000)),
            main_category=Category.objects.get(slug='level2-first-sub')
        ).save()
        Product(
            name='Product 2',
            slug=slugify('Product 2'),
            active=True,
            unit_price=Decimal(random.randint(50, 1000)),
            main_category=Category.objects.get(slug='level1-first')
        ).save()
        Product(
            name='Product 3',
            slug=slugify('Product 3'),
            active=True,
            unit_price=Decimal(random.randint(50, 1000)),
            main_category=Category.objects.get(slug='level1-second')
        ).save()
                
    def test_product_adds_additional_categories(self):
        p = Product(
            name='Product 4',
            slug=slugify('Product 4'),
            active=True,
            unit_price=Decimal(random.randint(50, 1000)),
            main_category=Category.objects.get(slug='level1-second')
        )
        
        p.save()
        self.assertEqual(p.additional_categories.all()[0].slug, 'level1-second')
        
    def test_product_absolute_url(self):
        self.assertEqual(Product.objects.get(slug='product-1').get_absolute_url(), 
            '/shop/catalog/top-category/level1-first/level2-first/level2-first-sub/product/product-1/')
            
    def test_product_detail(self):
        product_url = Product.objects.get(slug='product-1').get_absolute_url()
        response = self.client.get(product_url)
        self.assertContains(response, '/shop/catalog/top-category/level1-first/level2-first/level2-first-sub/product/product-1/')
                
    def test_list_products_in_category(self):
        category = Category.objects.get(slug='level1-first')
        response = self.client.get(category.get_absolute_url())
        self.assertContains(response, '/shop/catalog/top-category/level1-first/level2-first/level2-first-sub/product/product-1/')
        self.assertContains(response, '/shop/catalog/top-category/level1-first/product/product-2/')
        self.assertNotContains(response, '/shop/catalog/top-category/level1-second/product/product-3/')
        category = Category.objects.get(slug='level1-second')
        response = self.client.get(category.get_absolute_url())
        self.assertNotContains(response, '/shop/catalog/top-category/level1-first/level2-first/level2-first-sub/product/product-1/')
        self.assertNotContains(response, '/shop/catalog/top-category/level1-first/product/product-2/')
        self.assertContains(response, '/shop/catalog/top-category/level1-second/product/product-3/')