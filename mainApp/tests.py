from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class IndexPageTests(TestCase):
	def test_index_status_code(self):
		url = reverse('index')
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)
