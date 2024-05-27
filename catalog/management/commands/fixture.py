from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Загружает данные из фикстуры'

    def handle(self, *args, **options):
        call_command('loaddata', 'fixture/products.json')
