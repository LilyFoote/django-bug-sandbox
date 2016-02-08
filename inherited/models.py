from django.db import models


class Base(models.Model):
    pass


class Child(Base):
    name = models.CharField(max_length=255)
