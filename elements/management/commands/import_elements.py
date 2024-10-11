import csv
from django.core.management.base import BaseCommand
from elements.models import Element

class Command(BaseCommand):
    help = 'Imports elements data from a CSV file'

    def handle(self, *args, **kwargs):
        # Убедитесь, что путь к вашему CSV файлу правильный
        file_path = 'elements_data.csv'

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Element.objects.update_or_create(
                    atomic_number=row['atomic_number'],
                    defaults={
                        'name': row['name'],
                        'symbol': row['symbol'],
                        'category': row['category'],
                        'description': row['description'],
                        'application': row['application'],
                        'fact': row['fact'],
                        'wiki_link': row['wiki_link'],
                    }
                )

        self.stdout.write(self.style.SUCCESS('Successfully imported elements data'))
