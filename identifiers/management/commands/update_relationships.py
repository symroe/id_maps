import csv

import requests
import glob2

from django.core.management.base import BaseCommand


from identifiers.utils import update_relationships


class Command(BaseCommand):
    def handle(self, *args, **options):
        update_relationships()
