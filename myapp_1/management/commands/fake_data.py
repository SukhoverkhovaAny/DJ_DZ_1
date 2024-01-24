from django.core.management.base import BaseCommand
from myapp_1.models import Client, Order, Product

import random


class Command(BaseCommand):
    help = "generate fake data"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help="Client ID")

    def handle(self, *args, **kwargs):
        client_list = []
        product_list = []
        count = kwargs.get('count')

        for j in range(10):
            product = Product(name=f'PName{j}', description=f'text-{j}', price=f'{j+1}0', quantity=f'{j}')
            product.save()
            product_list.append(product)

        for i in range(1, count + 1):
            client = Client(name=f'Name{i}', email=f'mail{i}.mail.ru', phone=f'123-{i}', address=f'address{i}')
            client.save()
            client_list.append(client)

        for k in range(1, 6): # количесво заказов
            client_rnd = random.randint(0, count-1) # выбираем рандомного покупателя
            order = Order(customer=client_list[client_rnd])
            total_price = 0
            for l in range(0, 10):
                if random.randint(0,1) == 1: # выбираем рандомные товары
                    total_price += float(product_list[l].price)
                    order.total_price = total_price
                    order.save()
                    order.products.add(product_list[l])

