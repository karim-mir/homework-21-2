from catalog.models import Product
from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy, reverse


class ProductListView(ListView):
    model = Product
    template_name = "catalog/catalog_list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/catalog_detail.html"


class ProductCreateView(CreateView):
    model = Product
    template_name = "catalog/product_form.html"
    fields = ("name", "description", "photo", "category", "price")
    success_url = reverse_lazy("catalog:catalog_list")


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "catalog/product_form.html"
    fields = ("name", "description", "photo", "category", "price")
    success_url = reverse_lazy("catalog:catalog_list")

    def get_success_url(self):
        return reverse("catalog:catalog_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:catalog_list")



class ContactView(TemplateView):
    template_name = "catalog/contact.html"
