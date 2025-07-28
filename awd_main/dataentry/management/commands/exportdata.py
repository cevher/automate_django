from django.core.management.base import BaseCommand

from dataentry.models import Student
from django.apps import apps
import csv

from django.apps import apps
from datetime import datetime

class Command(BaseCommand):
    help = "Export data from database to a CSV file."
    
    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='Model name')
    
    def handle(self, *args, **kwargs):
        students = Student.objects.all()
        model_name = kwargs['model_name'].capitalize()
        
        model=None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                pass
        if not model:
            self.stderr.write(f"model {model_name} could not found!")
            return
        
        data = model.objects.all()
        
        timestamp= datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        
        file_path = f"exported_{model_name}_data_{timestamp}.csv"
        
        # Open file to write
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            
            # we should write the field names of the given model dynamically
            writer.writerow([field.name for field in model._meta.fields])
            
            for dt in data:
                writer.writerow([getattr(dt, field.name) for field in model._meta.fields])

        self.stdout.write(self.style.SUCCESS('Data exported successfully.'))
        