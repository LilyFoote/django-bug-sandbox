from django.db.models import F
from django.test import TestCase

from .models import Child


class TestCopyField(TestCase):
    def test_copy_base_name(self):
        Child.objects.create(base_name='Base')

        Child.objects.update(name=F('base_name'))

        child = Child.objects.get()
        self.assertEqual(child.name, 'Base')

    def test_copy_name(self):
        Child.objects.create(name='Child')

        Child.objects.update(base_name=F('name'))

        child = Child.objects.get()
        self.assertEqual(child.name, 'Child')
