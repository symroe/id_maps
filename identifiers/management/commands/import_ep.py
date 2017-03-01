import csv

import requests
import glob2

from django.core.management.base import BaseCommand


from identifiers.utils import create_ids


class Command(BaseCommand):

    def parse_popolo_ids(self, data):
        for person in data.get('persons', []):
            if 'identifiers' in person:
                data = {
                    x['scheme']: x['identifier']
                    for x in person['identifiers']}

                for key, value in data.items():
                    create_ids(value, key, relations=data)

    def handle(self, *args, **options):

        req = requests.get("https://raw.githubusercontent.com/everypolitician/everypolitician-data/master/countries.json")
        for instance in req.json():
            for legislature in instance['legislatures']:
                req = requests.get(legislature['popolo_url'])
                self.parse_popolo_ids(req.json())
