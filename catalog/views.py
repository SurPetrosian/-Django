from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    products = Product.objects.all()
    context = {
        'products': products

    }
    return render(request, 'catalog/home.html', context=context)


def contacts(request):
    return render(request, 'catalog/contacts.html')


def products(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product

    }
    return render(request,'catalog/products.html', context=context)