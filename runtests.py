#!/usr/bin/env python
from djeasytests.runtests import runtests_parse
from shop_categories.test_utils.cli import configure
    
if __name__ == '__main__':    
    runtests_parse(configure=configure,
        test_labels_prefix='shop_categories',
        default_test_labels=['shop_categories'],
        tmp_dir_prefix='django-shop-categories',
        ROOT_URLCONF='shop_categories.test_utils.project.urls')