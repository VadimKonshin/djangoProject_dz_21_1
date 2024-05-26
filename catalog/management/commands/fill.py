from django.core.management.base import BaseCommand
from catalog.models import Product


class Command(BaseCommand):
    help = 'Displays the number of products'

    def handle(self, *args, **kwargs):
        count = Product.objects.count()
        self.stdout.write(f'There are {count} products.')
