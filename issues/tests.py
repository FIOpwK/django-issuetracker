from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from issues.models import Issue

from issues.views import home_page


# Create your tests here.
class HomePageTest(TestCase):
    [...]

    def test_only_saves_issues_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Issue.objects.count(), 0)

    def test_home_page_returns_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'issue_text': 'A new issue item'})
        self.assertEqual(Issue.objects.count(), 1)
        new_issue = Issue.objects.first()
        self.assertEqual(new_issue.text, 'A new issue item')

        self.assertIn('A new issue item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Issue()
        first_item.text = 'The first (ever) issue item'
        first_item.save()

        saved_items = Issue.objects.all()
        self.assertEqual(saved_items.count(), 1)

        first_saved_item = saved_items[0]
        self.assertEqual(first_saved_item.text, 'The first (ever) issue item')
