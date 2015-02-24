from django.test import TestCase
from django.core.urlresolvers import resolve
from sections.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
    
    def test_test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)