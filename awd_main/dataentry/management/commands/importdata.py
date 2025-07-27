from django.core.management.base import BaseCommand, CommandError

from dataentry.models import Student
import csv

from django.apps import apps


class Command(BaseCommand):
    help ="Import data from CSV file"
    
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Data file path')
        parser.add_argument('model_name', type=str, help='Model name')
    
    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()
        model = None
        # Search for the model accross all installed apps
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break #stop searchin once the model is found
            except LookupError:
                continue #model not found in this app continue to search in next app
        if not model:
            raise CommandError(f'Model "{model} not found imn any app')
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS('Data inserted successfully from CSV!'))