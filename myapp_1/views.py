from django.shortcuts import render
from django.http import HttpResponse
import logging
from datetime import datetime, timedelta
from .models import Client, Order, Product
from .forms import ProductFormWidget, ProductChoiceForm
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect


logger = logging.getLogger(__name__)


def main(request):
    logger.info('Main page accessed')
    http_1 = """<!doctype html>
                <html lang="ru">
                <head>
                    <meta charset="utf-8">
                    <title>Мой первый Django сайт</title>
                </head>
                <body>
                    <h1>Привет, друг!</h1>
                    <h2>Приветствую на моем первом Django сайте!</h2>
                    <p>Я очень старалась его создать, надеюсь тебе понравится!</p>
                    <p>Держи котика)</p>
                    <img src="myproject/image/cat.jpg">
                <footer>
                    <p>Все права защищены©.</p>
                </footer>
                </body>
                </html>
    """
    return HttpResponse(http_1)


def about_me(request):
    logger.info('About_me page accessed')
    http_2 = """<!doctype html>
                <html lang="ru">
                <head>
                    <meta charset="utf-8">
                    <title>Обо мне</title>
                </head>
                <body>
                    <h2>Меня зовут Аня, я являюсь студентом GeekBrains!</h2>
                    <p>Обучаюсь на Python-разработчика.</p>
                    <p>Это совершенно новая сфера для меня, но мне очень нравится, и я вкладываю в обучение много сил и времени)</p>
                <footer>
                    <p>Все права защищены©.</p>
                </footer>
                </body>
                </html>
    """
    return HttpResponse(http_2)


def basket(request, client_id):
    products = []
    client = Client.objects.filter(pk=client_id).first()
    orders = Order.objects.filter(customer=client).all()
    for order in orders:
        products.append(order.products.all())
    products.reverse()
    return render(request, 'myapp_1/client_all_orders.html', {'client': client, 'orders': orders, 'products': products})


def sorted_basket(request, client_id, days_ago):
    products = []
    product_set = []
    now = datetime.now()
    before = now - timedelta(days=days_ago)
    client = Client.objects.filter(pk=client_id).first()
    orders = Order.objects.filter(customer=client, date_ordered__range=(before, now)).all()
    for order in orders:
        products = order.products.all()
        for product in products:
            if product not in product_set:
                product_set.append(product)

    return render(request, 'myapp_1/client_all_product.html', {'client': client, 'product_set': product_set, 'days': days_ago})


def product_update_form(request, product_id):
    if request.method == 'POST':
        form = ProductFormWidget(request.POST, request.FILES)
        if form.is_valid():
            # Делаем что-то с данными
            logger.info(f'Получили {form.cleaned_data=}.')
            name = form.cleaned_data.get('name')
            price = form.cleaned_data.get('price')
            description = form.cleaned_data.get('description')
            number = form.cleaned_data.get('number')

            image = request.FILES['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)

            product = Product.objects.filter(pk=product_id).first()
            product.name = name
            product.price = price
            product.description = description
            product.quantity = number
            product.image = image.name
            product.save()

    else:
        form = ProductFormWidget()
    return render(request, 'myapp_1/product_update.html', {'form': form})


def product_update_id_form(request):
    if request.method == 'POST':
        form = ProductChoiceForm(request.POST)
        if form.is_valid():
            logger.info(f'Получили {form.cleaned_data=}.')
            prod_id = form.cleaned_data.get('product_id') # получил id продукта - номер из выпадающего списка
            response = redirect(f'/DZ_1/product_update/{prod_id}')
            return response
    else:
        form = ProductChoiceForm()
    return render(request, 'myapp_1/product_update_id.html', {'form': form})



# Create your views here.
