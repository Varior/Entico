from django.views.generic import DetailView, ListView
from .models import Category, Product, ProductImages

class ProductList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/product/list.html' 

    def get_context_data(self, *args, **kwargs): 
        context = super(ProductList, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()        
        return context

class ProductListByCategory(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/product/list.html'
    allow_empty = False
 
    def get_queryset(self):
        category = Category.objects.filter(slug = self.kwargs.get('category_slug'))
        products = Product.objects.filter(category = category)
        return products

    def get_context_data(self, *args, **kwargs): 
        context = super(ProductListByCategory, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['category'] = Category.objects.get(slug = self.kwargs.get('category_slug'))
        return context

class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'shop/product/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context