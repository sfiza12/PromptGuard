from django.test import TestCase
from django.urls import reverse

class WebViewsTestCase(TestCase):
    def test_alumni_view(self):
        response = self.client.get(reverse('alumni'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alumni.html')
        self.assertContains(response, 'Alumni & Mentors')
        self.assertContains(response, 'Dr. Evelyn Chen')
        self.assertContains(response, 'Marcus Vance')
        self.assertContains(response, 'Priya Nair')

