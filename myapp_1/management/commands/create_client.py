from django.core.management.base import BaseCommand
from myapp_1.models import Client, Order, Product


class Command(BaseCommand):
    help = "Create Client"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="Client Name")
        parser.add_argument("email", type=str, help="Client email")
        parser.add_argument("password", type=str, help="Client password")
        parser.add_argument("phone", type=str, help="Client phone")
        parser.add_argument("address", type=str, help="Client address")

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        password = kwargs.get('password')
        phone = kwargs.get('phone')
        address = kwargs.get('address')

        client = Client(name=name, email=email, password=password, phone=phone, address=address)
        client.save()

        self.stdout.write(f'{client}')