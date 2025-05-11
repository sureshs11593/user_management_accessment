from django.core.management.base import BaseCommand
from users.models import UserProfile
from faker import Faker

class Command(BaseCommand):
    help = 'Populate the database with dummy users'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):
            UserProfile.objects.create(
                full_name=fake.name(),
                email=fake.unique.email(),
                is_active=True
            )
        self.stdout.write(self.style.SUCCESS('Successfully created 10 users'))
