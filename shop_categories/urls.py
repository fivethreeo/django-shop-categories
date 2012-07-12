from django.conf.urls.defaults import patterns, url
from django.shortcuts import get_object_or_404

from shop.views import ShopListView
from shop.views.product import ProductDetailView
from shop.models.productmodel import Product
from shop_categories.models import Category

class CategoryShopListView(ShopListView):
    
    def get_queryset(self):
        category = get_object_or_404(Category, path=self.kwargs['path'])
        self.category = category
        queryset = super(CategoryShopListView, self).get_queryset()
        return queryset.filter(additional_categories__lft__gte=category.lft, additional_categories__rght__lte=category.rght).distinct()
        
    def get_context_data(self, **kwargs):
        context = super(CategoryShopListView, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context
        
class CategoryProductDetailView(ProductDetailView):
    
    def get_queryset(self):
        queryset = super(CategoryProductDetailView, self).get_queryset()
        return queryset.filter(main_category__path=self.kwargs['path'])
        
    def get_context_data(self, **kwargs):
        context = super(CategoryProductDetailView, self).get_context_data(**kwargs)
        category = get_object_or_404(Category, path=self.kwargs['path'])
        context['category'] = category
        return context
        
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