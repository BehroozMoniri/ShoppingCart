from django.core.management.base import BaseCommand
from core.models import Product

class Command(BaseCommand):
    help = 'Load product data to the database'

    def handle(self, *args, **kwargs):
        Product.objects.get_or_create(
            name= 'Pizza',
            price = 5.50
        )

        Product.objects.get_or_create(
            name= 'Bread',
            price = 1.50
        )
        Product.objects.get_or_create(
            name= 'Soap',
            price = 0.50
        )

        Product.objects.get_or_create(
            name= 'Potatos',
            price = 1.50
        )
        Product.objects.get_or_create(
            name= 'Milk',
            price = 0.50
        )
        Product.objects.get_or_create(
            name= 'Cheese',
            price = 3.50
        )