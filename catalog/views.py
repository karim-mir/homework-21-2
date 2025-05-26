from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from django.urls import reverse_lazy, reverse

from catalog.models import Product, Category
from catalog.forms import ProductForm, ProductModeratorForm
from catalog.services import get_products_from_cache, get_products_by_category


class ProductListView(ListView):
    model = Product
    template_name = "catalog/catalog_list.html"
    context_object_name = "products"


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/catalog_detail.html"

    def get_queryset(self):
        return get_products_from_cache()


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "catalog/product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:catalog_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Установите владельца товара
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = "catalog/product_form.html"

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner or user.has_perm("catalog.can_unpublish_product"):
            return ProductForm  # Или другой класс формы для модераторов
        raise PermissionDenied("У вас нет прав на редактирование этого продукта.")

    def get_success_url(self):
        return reverse("catalog:catalog_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:catalog_list")

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if request.user != product.owner and not request.user.has_perm("catalog.can_delete_product"):
            raise PermissionDenied("У вас нет прав на удаление этого продукта.")
        return super().dispatch(request, *args, **kwargs)


class ProductListByCategoryView(ListView):
    model = Product
    template_name = "catalog/catalog_list_by_category.html"
    context_object_name = "products"

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        return get_products_by_category(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, id=self.kwargs.get("category_id"))
        context["category"] = category
        return context


class ContactView(TemplateView):
    template_name = "catalog/contact.html"
