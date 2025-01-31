from django.contrib.auth.models import User
from django.core.management import BaseCommand
from crm.settings import env


class Command(BaseCommand):
    def handle(self, *args, **options):
        username = env('USER', default='admin')
        email = env('EMAIL', default='catsdogs@gmail.com')
        password = env('PASS', default='aqnda337f')
        try:
            result = User.objects.get(username=username, email=email)
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" already exist.'))
        except User.DoesNotExist:
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" was created successfully.'))
