from django.db import models

from foo.models import Bar


class Foo(models.Model):
    name = models.CharField(max_length=255)
    bars = models.ManyToManyField(Bar, related_name='+')
