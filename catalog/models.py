from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )

    description = models.TextField(
        max_length=150, verbose_name="Опсиание", help_text="Введите описание продукта"
    )

    photo = models.ImageField(
        upload_to="catalog/photo",
        verbose_name="Изображение",
        help_text="Загрузите иображение продукта",
    )

    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию продукта",
        null=True,
        blank=True,
        related_name="products"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
        help_text="Введите цену продукта",
    )

    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания продукта",
    )

    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения",
        help_text="Введите дату последнего изменения продукта",
    )


class Meta:
    verbose_name = "Продукт"
    verbose_name_plural = "Продукты"
    ordering = ["category", "name", "price", "created_date"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )

    description = models.TextField(
        max_length=150,
        verbose_name="Опсиание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )


class Meta:
    verbose_name = "Категория"
    verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
