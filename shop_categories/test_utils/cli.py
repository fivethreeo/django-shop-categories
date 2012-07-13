# -*- coding: utf-8 -*-
import os

gettext = lambda s: s

urlpatterns = []

DJANGO_SETTINGS_MODULE = 'shop_categories.test_utils.cli' # this module
ROOT_URLCONF = DJANGO_SETTINGS_MODULE

def configure(**extra):
    from django.conf import settings
    os.environ['DJANGO_SETTINGS_MODULE'] = DJANGO_SETTINGS_MODULE
    defaults = dict(
        CACHE_BACKEND = 'locmem:///',
        DEBUG = True,
        TEMPLATE_DEBUG = True,
        DATABASE_SUPPORTS_TRANSACTIONS = True,
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        SITE_ID = 1,
        USE_I18N = True,
        MEDIA_ROOT = '/media/',
        STATIC_ROOT = '/static/',
        MEDIA_URL = '/media/',
        STATIC_URL = '/static/',
        ADMIN_MEDIA_PREFIX = '/static/admin/',
        EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend',
        SECRET_KEY = 'key',
        TEMPLATE_LOADERS = (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
            'django.template.loaders.eggs.Loader',
        ),
       TEMPLATE_CONTEXT_PROCESSORS = [
            "django.contrib.auth.context_processors.auth",
            "django.core.context_processors.i18n",
            "django.core.context_processors.debug",
            "django.core.context_processors.request",
            "django.core.context_processors.media",
            'django.core.context_processors.csrf',
            "django.core.context_processors.static"
        ],
        MIDDLEWARE_CLASSES = [
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.doc.XViewMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware'
        ],
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
        LANGUAGE_CODE = "en",
        LANGUAGES = (
            ('en', gettext('English')),
            ('fr', gettext('French')),
            ('de', gettext('German')),
            ('pt-BR', gettext("Brazil")),
            ('nl', gettext("Dutch")),
        ),
        SOUTH_TESTS_MIGRATE = False,
        ROOT_URLCONF = ROOT_URLCONF,
        SHOP_PRODUCT_MODEL = 'shop_categories.test_utils.project.models.product.Product',
        SHOP_CATEGORIES_CATEGORY_MODEL = 'shop_categories.test_utils.project.models.category.Category'
    )
    defaults.update(extra)
    settings.configure(**defaults)