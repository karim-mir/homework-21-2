from django.core.management.base import BaseCommand
from catalog.models import Product  # Импортируйте вашу модель продукта


class Command(BaseCommand):
    help = "Добавляет тестовые продукты в базу данных после удаления существующих"

    def handle(self, *args, **kwargs):
        # Удаляем все существующие продукты
        Product.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Все существующие продукты удалены."))

        # Добавляем тестовые продукты
        test_products = [
            {"name": "Тестовый продукт 1", "price": 100},
            {"name": "Тестовый продукт 2", "price": 200},
            {"name": "Тестовый продукт 3", "price": 300},
        ]

        for product_data in test_products:
            product = Product(**product_data)
            product.save()

        self.stdout.write(self.style.SUCCESS("Тестовые продукты добавлены."))
