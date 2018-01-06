from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<category_slug>[-\w]+)/$', views.ProductList, name='ProductListByCategory'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<slug>[-\w]+)/$', views.ProductDetail, name='ProductDetail'),
    url(r'^$', views.ProductList, name='ProductList'),
]