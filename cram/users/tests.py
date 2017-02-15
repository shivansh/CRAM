from django.core.urlresolvers import resolve
from django.test import TestCase
from users.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
from users.models import Item

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

    def test_save_item_when_required(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.count(), 0)

    def test_save_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

        # The following test is now no longer required since we now redirect
        """
        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string(
                'home.html',
                {'new_item_text': 'A new list item'}
                )
        self.assertEqual(response.content.decode(), expected_html)
        """

    def test_redirect_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_displays_all_items(self):
        Item.objects.create(text='Item 1')
        Item.objects.create(text='Item 2')

        request = HttpRequest()
        response = home_page(request)
        self.assertIn('Item 1', response.content.decode())
        self.assertIn('Item 2', response.content.decode())

class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')