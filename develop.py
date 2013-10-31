#!/usr/bin/env python
from djeasytests.testsetup import TestSetup
test_settings = dict(
    SITE_ID=1,
    ROOT_URLCONF='shop_categories.test_utils.project.urls',
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'shopexampledb.sqlite',
        }
    },
    INSTALLED_APPS = [
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'django.contrib.sites',
        'django.contrib.staticfiles',
        'treeadmin',
        'shop_categories',
        'shop_categories.test_utils.project'
    ],
    SHOP_PRODUCT_MODEL = 'shop_categories.test_utils.project.models.product.Product',
    SHOP_CATEGORIES_CATEGORY_MODEL = 'shop_categories.test_utils.project.models.category.Category'
)

testsetup = TestSetup(appname='shop_categories', test_settings=test_settings)

if __name__ == '__main__':
    testsetup.run(__file__)
