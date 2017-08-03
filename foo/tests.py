from django.test import TestCase

from foo.models import Bar, Foo


class TestManyToManyField(TestCase):
    def test_add_bar_to_foo(self):
        bar = Bar.objects.create(name='Bar')
        foo = Foo.objects.create(name='Foo')

        foo.bars.add(bar)

        self.assertIn(bar, foo.bars.all())
