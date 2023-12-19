from django.shortcuts import render
from django.http import HttpResponse
import logging


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

# Create your views here.
