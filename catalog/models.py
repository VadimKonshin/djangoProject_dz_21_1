from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Название категории", help_text="Введите название категории", )
    description = models.TextField(verbose_name="Описание категории", help_text="Введите описание категории",
                                   **NULLABLE)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Название товара", help_text="Введите название товара")
    description = models.TextField(verbose_name="Описание товара", help_text="Введите описание товара", **NULLABLE)
    price = models.IntegerField(verbose_name='Цена', help_text='Введите цену товара')
    photo = models.ImageField(upload_to="products/photo", **NULLABLE, verbose_name="фото",
                              help_text="загрузите фото товара", )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    view_counter = models.PositiveIntegerField(verbose_name='Просмотры', default=0, **NULLABLE)

    owner = models.ForeignKey(User, verbose_name='владелец', **NULLABLE, on_delete=models.SET_NULL)

    # manufactured_at = models.DateField(auto_now=True, verbose_name='')
    # t_ext = models.TextField(verbose_name="Описание категории", help_text="Введите описание категории",
    #                                **NULLABLE)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price"]

    def __str__(self):
        return f"{self.name}"


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_num = models.IntegerField(default=0, verbose_name='номер версии')
    version_name = models.CharField(max_length=150, verbose_name='название версии')
    is_active = models.BooleanField(default=True, verbose_name='активно')

    def __str__(self):
        return f'{self.is_active}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
