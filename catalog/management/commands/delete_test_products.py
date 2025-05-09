from django.core.management.base import BaseCommand
from catalog.models import Product


class Command(BaseCommand):
    help = "Удаляет все тестовые продукты из базы данных"

    def handle(self, *args, **kwargs):
        # Удаляем все тестовые продукты
        deleted_count, _ = Product.objects.filter(
            name__startswith="Тестовый продукт"
        ).delete()

        if deleted_count:
            self.stdout.write(
                self.style.SUCCESS(f"Удалено {deleted_count} тестовых продуктов.")
            )
        else:
            self.stdout.write(
                self.style.WARNING("Нет тестовых продуктов для удаления.")
            )
