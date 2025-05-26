from django.core.cache import cache

from catalog.models import Product, Category
from config.settings import CACHE_ENABLED

def get_products_from_cache():
    """Получает данные по продукту из кэша, если кэш пуст, получает данные из БД."""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_products_by_category(category_id):
    """Возвращает список всех продуктов в указанной категории."""
    return Product.objects.filter(category_id=category_id)
