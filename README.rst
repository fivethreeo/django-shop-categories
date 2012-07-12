======================
django-shop-categories
======================

A generic payment app for Django using Netaxept

Installation
------------

For the current stable version:

:: 
 
    pip install django-shop-categories
    
For the development version:

::

    pip install -e git+git://github.com/fivethreeo/django-shop-categories.git#egg=django-shop-categories

Configuration
-------------

Add ``shop_categories`` to ``settings.INSTALLED_APPS``.

Set ``SHOP_PRODUCT_MODEL`` to ``shop_categories.models.default.CategoryProduct``.

Then run:

::

    manage.py syncdb

