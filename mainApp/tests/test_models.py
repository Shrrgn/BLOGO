from django.test import TestCase
from django.urls import reverse
from mainApp.models import Category, Post
from django.core.files.uploadedfile import SimpleUploadedFile #for image
# Create your tests here.

'''
class IndexPageTests(TestCase):
	def test_index_status_code(self):
		url = reverse('wrapper')
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)
'''
class CategoryModelTests(TestCase):
	
	@classmethod
	def setUpTestData(cls):
		Category.objects.create(name = 'Test category')

	def setUp(self):
		self.category = Category.objects.get(id = 1)

	def test_category_creation(self):
		self.assertTrue(isinstance(self.category, Category))

	def test_category_name(self):
		field_label = self.category._meta.get_field('name').verbose_name
		self.assertEquals(field_label, 'name')

	def test_category_slug(self):
		field_label = self.category._meta.get_field('slug').verbose_name
		self.assertEquals(field_label, 'slug')

	def test_category_str_name(self):
		self.assertEquals(self.category.name, str(self.category))

	def test_get_absolute_url(self):
		#absolute url will be written later
		pass


class PostModelTests(TestCase):pass

class CommentsModelTest(TestCase):pass