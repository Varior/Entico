from django.conf.urls import url
from .views import ProductList, ProductDetail, ProductListByCategory

urlpatterns = [
    url(r'^(?P<category_slug>[-\w]+)/(?P<slug>[-\w]+)/$', ProductDetail.as_view(), name='ProductDetail'),
    url(r'^(?P<category_slug>[-\w]+)/$', ProductListByCategory.as_view(), name='ProductListByCategory'),
    url(r'^$', ProductList.as_view(), name='ProductList'),
]