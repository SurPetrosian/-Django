from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/create_product.html'
    success_url = reverse_lazy('home')



class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/home.html'
    success_url = 'create product/'
    pk_url_kwarg = 'product_id'


class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/products.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'  # соответствие параметру из URL

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    pk_url_kwarg = 'product_id'
    success_url = '/'