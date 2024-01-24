from django.core.management.base import BaseCommand
from myapp_1.models import Product


class Command(BaseCommand):
    help = "Create product"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="product Name")
        parser.add_argument("description", type=str, help="product description")
        parser.add_argument("price", type=float, help="product price")
        parser.add_argument("quantity", type=int, help="product quantity")

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        description = kwargs.get('description')
        price = kwargs.get('price')
        quantity = kwargs.get('quantity')

        product = Product(name=name, description=description, price=price, quantity=quantity)
        product.save()

        self.stdout.write(f'{product}')
