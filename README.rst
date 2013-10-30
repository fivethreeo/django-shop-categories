======================
django-shop-categories
======================

A extendable category app using django-mptt for django-shop.

.. image:: https://travis-ci.org/fivethreeo/django-shop-categories.png?branch=develop
   :target: https://travis-ci.org/fivethreeo/django-shop-categories

Installation
------------

For the current stable version:

:: 
 
    pip install django-shop-categories
    
For the development version:

::

    pip install -e git+git://github.com/fivethreeo/django-shop-categories.git#egg=django-shop-categories

Running tests:

::

    git clone git://github.com/fivethreeo/django-shop-categories.git
    cd django-shop-categories
    virtualenv test_env
    source ./test_env/bin/activate
    pip install -r requirements.txt
    python runtests.py  
    
Configuration
-------------

Add ``shop_categories`` and ``treeadmin`` to ``settings.INSTALLED_APPS``.

Set ``SHOP_PRODUCT_MODEL`` to ``shop_categories.models.defaults.product.default.CategoryProduct``.

In your urls.py add this **before** your shop patterns:

::
    
    urlpatterns += patterns('',
        url(r'^catalog/', include('shop_categories.urls')),
    )   

Then run:

::

    manage.py syncdb

Extending the Category model
----------------------------

In your own app make a models dir with __init__.py and a category.py dir, like so:

::

    app/models/__init__.py
    app/models/category.py

Note: Do not import the model from category.py in __init__.py, the model should NOT be in a "real" models module as this will cause the overridden Category model to be defined twice. 

In category.py:

:: 

    from django.db import models
    from shop_categories.models.defaults.category.base import ProductCategoryBase
            
    class Category(ProductCategoryBase):
        
        image = models.ImageField(upload_to='categoryimages/', null=True, blank=True)
    
        class Meta:
            abstract = False
            app_label = 'app'

Set ``SHOP_CATEGORIES_CATEGORY_MODEL`` to ``('app.models.category.Category, 'app')``

Register your custom category model in admin.py:

::

    from shop_categories.models import Category
    from shop_categories.admin import ProductCategoryAdmin

    admin.site.register(Category, ProductCategoryAdmin)


Then, assuming your Product model is not already synced, run:

::

    manage.py syncdb

Extending the Product model
----------------------------

When extending Product models in your shop make sure they subclass from ``shop_categories.models.defaults.product.base.CategoryProductBase`` to add the Category Foreignkey and M2M fields.

Example implementation
----------------------
An example of a django-shop with django-shop-categories can be found here: https://github.com/fivethreeo/django-shop-example
