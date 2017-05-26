from django.db import models


class One(models.Model):
    name = models.CharField(max_length=255)
    twos = models.ManyToManyField(
        'Two',
        through='One2Two',
    )


class Two(models.Model):
    name = models.CharField(max_length=255)


class One2Two(models.Model):
    one = models.ForeignKey(One)
    two = models.ForeignKey(Two)

    class Meta:
        unique_together = ('one', 'two')
