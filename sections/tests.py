from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.shortcuts import render
from django.template.loader import render_to_string

from sections.views import home_page
from sections.models import Item, List

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
    
    #def test_home_page_only_saves_items_when_necessary(self):
        #request = HttpRequest()
        #home_page(request)
        #self.assertEqual(Item.objects.count(), 0)
        
    #def test_home_page_displays_all_list_items(self):
        #Item.objects.create(text='email')
        #Item.objects.create(text='phone_number')
        
        #request = HttpRequest()
        #response = home_page(request)
        
        #self.assertIn('email', response.content.decode())
        #self.assertIn('phone_number', response.content.decode())
        
        
class NewListTest(TestCase):
    
    def test_saving_a_POST_requst(self):
        self.client.post(
                         '/sections/new',
                         data={'user_name': 'Kamau'}
                         )
        #request = HttpRequest()
        #request.method = 'POST'
        #request.POST['user_name'] = 'Kamau'
        
        #response = home_page(request)
        
        self.assertEqual(Item.objects.count(), 1)
        new_user = Item.objects.first()
        self.assertEqual(new_user.text, 'Kamau')
        
        #self.assertEqual(response.status_code, 302)
        #self.assertEqual(response['location'], 'sections/kamaus-only/')
        #self.assertIn('Kamau', response.content.decode())
        #expected_html = render_to_string('home.html',
        #                                 {'new_user_name': 'Kamau'}
        #                                 )
        #self.assertEqual(response.content.decode(), expected_html)
        
    def test_redirects_after_POST(self):
        response = self.client.post(
                         '/sections/new',
                         data={'user_name': 'Kamau'}
                         )        
        
        #request = HttpRequest()
        #request.method = 'POST'
        #request.POST['user_name'] = 'Kamau'
        
        #response = home_page(request)
        
        self.assertRedirects(response, '/sections/kamaus-only/')
        
        #self.assertEqual(response.status_code, 302)
        #self.assertEqual(response['location'], 'sections/kamaus-only/')
                
        
        
        
class ListAndItemModelTest(TestCase):
    
    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()
        
        
        first_item = Item()
        first_item.text = 'The first ever item'
        first_item.list = list_
        first_item.save()
        
        second_item = Item()
        second_item.text = 'The second item'
        second_item.list = list_
        second_item.save()
        
        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)
        
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first ever item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'The second item')
        self.assertEqual(second_saved_item.list, list_)
        
class ListViewTest(TestCase):
    
    def test_uses_sections_template(self):
        list_ = List.objects.create()
        response = self.client.get('sections/%d/',(list_.id,))
        self.assertTemplateNotUsed(response, 'home.html')
        
    def test_displays_only_items_for_that_list(self):
        correct_list = List.objects.create()
        Item.objects.create(text='itemey 1', list=correct_list)
        Item.objects.create(text='itemey 2', list=correct_list)
        other_list = List.objects.create()
        Item.objects.create(text='other list itemy 1', list=other_list)
        Item.objects.create(text='other list itemy 2', list=other_list)
        
        response = self.client.get('/sections/%d/' %(correct_list.id,))
        
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertContains(response, 'other list itemy 1')
        self.assertContains(response, 'other list itemy 1')
        
        
        
        