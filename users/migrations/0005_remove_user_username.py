# Generated by Django 4.2.2 on 2024-07-01 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_user_token"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
    ]
