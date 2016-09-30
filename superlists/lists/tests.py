from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page

class HomePageTest(TestCase):
    def test_root_resolves(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
