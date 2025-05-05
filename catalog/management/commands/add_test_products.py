from django.core.management.base import BaseCommand
from catalog.models import Product, Category  # Импортируйте вашу модель продукта и категорию
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = "Добавляет тестовые продукты в базу данных после удаления существующих"

    def handle(self, *args, **kwargs):
        # Удаляем все существующие продукты
        Product.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Все существующие продукты удалены."))

        # Создаем тестовую категорию (если необходимо)
        category, created = Category.objects.get_or_create(name="Тестовая категория")

        # Добавляем тестовые продукты
        test_products = [
            {
                "name": "Тестовый продукт 1",
                "description": "Описание тестового продукта 1",
                "price": 100.00,
                "category": category,
                "photo": None  # Здесь можно указать путь к изображению, если оно есть
            },
            {
                "name": "Тестовый продукт 2",
                "description": "Описание тестового продукта 2",
                "price": 200.00,
                "category": category,
                "photo": None
            },
            {
                "name": "Тестовый продукт 3",
                "description": "Описание тестового продукта 3",
                "price": 300.00,
                "category": category,
                "photo": None
            },
        ]

        for product_data in test_products:
            product = Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                category=product_data["category"],
            )

            product.save()

        self.stdout.write(self.style.SUCCESS("Тестовые продукты добавлены."))
