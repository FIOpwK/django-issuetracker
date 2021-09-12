from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from issues.views import home_page


# Create your tests here.
class HomePageTest(TestCase):

    def test_home_page_returns_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'issue_text': 'A new issue item'})
        self.assertIn('A new issue item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
