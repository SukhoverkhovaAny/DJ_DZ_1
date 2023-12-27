from django.core.management.base import BaseCommand
from myapp_1.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(name='John', email='john@example.com', phone=+79112234567, address='some location')
        client.save()
        self.stdout.write(f'{client}')
