from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

class HomePageTest(TestCase):
    def test_root_resolves(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')

        self.assertEqual(response.content.decode(), expected_html)
        # self.assertTrue(response.content.startswith(b'<html>'))
        # self.assertIn(b'<title>To-Do lists</title>', response.content)
        # self.assertTrue(response.content.strip().endswith(b'</html>'))
        # print (repr(response.content))
