from django.core.management.base import BaseCommand
import json
import os
from parser.models.models import MainSites
from django.conf import settings


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        fixture_path = os.path.join(settings.BASE_DIR, 'fixtures', 'initial_sites.json')

        if not os.path.exists(fixture_path):
            self.stdout.write(self.style.ERROR(f'Fixture file not found: {fixture_path}'))
            return

        with open(fixture_path, 'r') as file:
            data = json.load(file)

        for item in data:
            model_name = item.get('model')
            if model_name == 'parser.mainsites':
                url = item.get('fields').get('url')
                type = item.get('fields').get('type')
                MainSites.objects.get_or_create(url=url, type=type)

        self.stdout.write(self.style.SUCCESS('Successfully loaded initial data'))
