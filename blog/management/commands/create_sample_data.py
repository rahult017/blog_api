# blog/management/commands/create_sample_data.py
import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Blog
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = 'Create sample data for the Blog model'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of blog records to create')

    def handle(self, *args, **options):
        count = options['count']
        self.stdout.write(self.style.SUCCESS(f'Creating {count} sample blog records...'))

        # Create a superuser for authoring blogs
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin'
        )

        # Create sample blog data
        for _ in range(count):
            title = fake.catch_phrase()
            content = fake.paragraph(random.randint(3, 6))
            Blog.objects.create(
                title=title,
                content=content,
                author=admin_user
            )

        self.stdout.write(self.style.SUCCESS(f'{count} sample blog records created successfully.'))
