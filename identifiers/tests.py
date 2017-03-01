from collections import namedtuple

from django.test import TestCase

from identifiers.utils import create_ids, data_to_ids


class TestRelationships(TestCase):



    def test_create_identifiers(self):

        Row = namedtuple('row', ['local_authority_eng', 'gss'])

        data = [
            {
                'a': 1,
                'b': 2,
            }
        ]
        data_to_ids(data)
