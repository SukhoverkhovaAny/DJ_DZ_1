from django.core.management.base import BaseCommand
from myapp_1.models import Client, Order, Product


class Command(BaseCommand):
    help = "Generate fake client and order."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'Name{i}', email=f'mail{i}@mail.ru', phone=f'+7999888776{i}',
                            address=f'City{i}, Street{i}, House{i}')
            client.save()

