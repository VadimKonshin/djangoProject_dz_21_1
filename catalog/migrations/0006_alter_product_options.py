# Generated by Django 4.2.2 on 2024-07-05 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_product_is_published"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name", "price"],
                "permissions": (
                    ("set_published", "Can cancel publication of a product"),
                    ("change_description", "Can change description"),
                    ("change_category", "Can change category"),
                ),
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]
