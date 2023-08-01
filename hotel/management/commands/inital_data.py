from django.core.management.base import BaseCommand
from hotel.models import Hotel


class Command(BaseCommand):
    help = 'create inital data'

    def add_arguments(self, parser):
        pass

    def __str__(self):
        return str(self.name)

    def handle(self, *args, **options):
        hotels = [
            {
                "name": "Eve Harvey",
                "address": "Voluptates ullam qui totam quibusdam ut sunt fugiat animi lorem sint itaque consequuntur",
                "city": "alex",
                "country": "eygpt",
                "price_per_night": "242.00",
                "is_available": True
            },
            {
                "name": "Tatiana Watson",
                "address": "Voluptates ullam qui totam quibusdam ut sunt fugiat animi lorem sint itaque consequuntur",
                "city": "qatar",
                "country": "qatar",
                "price_per_night": "893.00",
                "is_available": True
            },
            {
                "name": "Hillary Morrow",
                "address": "Voluptates ullam qui totam quibusdam ut sunt fugiat animi lorem sint itaque consequuntur",
                "city": "giza",
                "country": "eygpt",
                "price_per_night": "50.00",
                "is_available": True
            },
            {
                "name": "Hillary Morrow",
                "address": "Voluptates ullam qui totam quibusdam ut sunt fugiat animi lorem sint itaque consequuntur",
                "city": "giza",
                "country": "eygpt",
                "price_per_night": "2.00",
                "is_available": True
            }
        ]
        try:
            for hotel in hotels:
                Hotel.objects.create(**hotel)

            self.stdout.write(self.style.SUCCESS(
                f'Successfully created hotels done'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(
                f'An Error occurred   {str(e)}'))
