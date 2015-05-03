from django.conf.urls import patterns, url
from shop_categories.views import CategoryProductDetailView, CategoryShopListView
from shop.models.productmodel import Product

urlpatterns = patterns('',
                       url(r'^(?P<path>.+)/product/(?P<slug>[0-9A-Za-z-_.//]+)/$',
                           CategoryProductDetailView.as_view(),
                           name='product_detail'
                           ),
                       url(r'^(?P<path>.+)/$',
                           CategoryShopListView.as_view(model=Product),
                           name='product_list'
                           ),
                       )
