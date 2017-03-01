import csv

from django.core.management.base import BaseCommand

import glob2

from identifiers.utils import data_to_ids, update_relationships


class Command(BaseCommand):

    def handle(self, *args, **options):
        for filename in glob2.iglob('data/**/*.tsv', with_matches=True):
            filename = filename[0]
            print(filename)
            with open(filename) as f:
                if filename.endswith('tsv'):
                    data = csv.DictReader(f, delimiter="\t")
                    data_to_ids(data)

        update_relationships()
