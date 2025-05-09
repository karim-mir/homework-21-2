from django.urls import path
from catalog.apps import CatalogConfig

from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, ContactView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="catalog_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="catalog_detail"),
    path("products/create/", ProductCreateView.as_view(), name="catalog_create"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="catalog_update"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="catalog_delete"),
    path("contact/", ContactView.as_view(), name="contact"),
]
