from django.db import models


class Bar(models.Model):
    name = models.CharField(max_length=255)


class Foo(models.Model):
    name = models.CharField(max_length=255)
    bars = models.ManyToManyField(Bar, related_name='+')
