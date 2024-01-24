from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    date_reg = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Client: {self.name}, email: {self.email},  phone: {self.phone}, address: {self.address}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Product name: {self.name}, description: {self.description}, price: {self.price}, quantity: {self.quantity}'


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Customer: {self.customer.name}, products: {self.products}, total_price: {self.total_price}, date_ordered: {self.date_ordered}'

# Create your models here.
