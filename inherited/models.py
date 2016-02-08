from django.db import models


class Base(models.Model):
    base_name = models.CharField(max_length=255)


class Child(Base):
    name = models.CharField(max_length=255)
