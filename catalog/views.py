from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView

from catalog.models import Product

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


# def products(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     context = {
#         'product': product
#
#     }
#     return render(request,'catalog/products.html', context=context)