from catalog.models import Product
from django.shortcuts import render, get_object_or_404


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products_list.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "product_detail.html", context)


def contact(request):
    return render(request, "contact.html")
