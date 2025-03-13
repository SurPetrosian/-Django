from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Add products to the database'

    def handle(self, *args, **options):
        category, _ = Category.objects.get_or_create(name='Самолеты', description='пассажирские самолеты')

        products = [
            {"name": "Airbus A380",
            "description": "широкофюзеляжный двухпалубный четырёхдвигательный турбореактивный пассажирский самолёт, "
                           "созданный концерном Airbus S.A.S.. ",
            "image": "",
            "category": category,
            "price": 105000,
            "created_at": "2025-03-13",
            "updated_at": "2025-03-13"},
            {"name": "Boeing 777",
             "description": "самый крупный в мире двухмоторный турбовентиляторный пассажирский самолёт.",
             "image": "",
             "category": category,
             "price": 100000,
             "created_at": "2025-03-13",
             "updated_at": "2025-03-13"}
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'successfully added product: {product.name}'))


