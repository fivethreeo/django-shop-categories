from setuptools import setup, find_packages
import os

import shop_categories

CLASSIFIERS = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
]

setup(
    name='django-shop-categories',
    version=shop_categories.get_version(),
    description='A extendable category app using django-mptt for django-shop',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Oyvind Saltvik',
    author_email='oyvind.saltvik@gmail.com',
    url='http://github.com/fivethreeo/django-shop-categories/',
    packages=find_packages(),
    package_data={
        'shop_categories': [
            'templates/shop_categories/*',
            'locale/*/LC_MESSAGES/*',
        ]
    },
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False,
    install_requires=['django-shop', 'django-mptt', 'django-treeadmin']
)
