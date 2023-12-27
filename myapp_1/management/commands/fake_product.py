from django.core.management.base import BaseCommand
from myapp_1.models import Product


class Command(BaseCommand):
    help = "Generate fake product."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            product = Product(name=f'Name{i}', description=f'Description{i}', price=f'10{i}10', quantity=i)
            product.save()
