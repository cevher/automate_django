from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Greets the user"
    
    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help="Specifies usrename")
    
    def handle(self, *args, **kwargs):
        name = kwargs['name']
        
        self.stdout.write( self.style.WARNING(f"Hi {name}, Good Morning"))