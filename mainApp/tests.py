from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class IndexPageTests(TestCase):
	def test_index_status_code(self):
		url = reverse('wrapper')
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)
'''
class CategoryPageTest(TestCase):
	def test_category_status_code(self):
		url = reverse('category_detail')
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)
'''