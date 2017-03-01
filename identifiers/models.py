from django.db import models


class Identifier(models.Model):
    code = models.CharField(blank=True, max_length=500, db_index=True)
    namespace = models.CharField(blank=True, max_length=500, db_index=True)

    def __str__(self):
        return "{}: {}".format(self.namespace, self.code)


class Relationship(models.Model):
    identifier = models.ForeignKey('Identifier', related_name='relationship', db_index=True)
    same_as = models.ForeignKey('Identifier', related_name='same_as', db_index=True)
