from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from sections.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
    
    def test_test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>', response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))
        
    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['user_name'] = 'The user name'
        
        response = home_page(request)
        
        self.assertIn('The user name', response.content.decode())
        expected_html = render_to_string(
                                         'home.html',
                                         {'new_user_name': 'The user name'}
                                         )
        self.assertEqual(response.content.decode(), expected_html)
        