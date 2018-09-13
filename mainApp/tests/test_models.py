from django.test import TestCase
from django.urls import reverse
from mainApp.models import Category, Post
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile #for image
from django.template.defaultfilters import slugify
import datetime
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
		Category.objects.create(name = 'Test category', slug = 'test-category')

	def setUp(self):
		self.category = Category.objects.get(id = 1)

	def test_category_creation(self):
		self.assertIsInstance(self.category, Category)

	def test_category_name(self):
		field_label = self.category._meta.get_field('name').verbose_name
		
		self.assertEquals(field_label, 'name')
		self.assertEquals(self.category.name, 'Test category')
		self.assertEquals(self.category._meta.get_field('name').max_length, 20)
		self.assertTrue(self.category._meta.get_field('name').unique, True)

	def test_category_slug(self):
		field_label = self.category._meta.get_field('slug').verbose_name
		
		self.assertEquals(field_label, 'slug')
		self.assertIsNotNone(self.category.slug)
		self.assertEquals(self.category.slug, slugify(self.category.name))

	def test_category_str_name(self):
		self.assertEquals(self.category.name, str(self.category))
	
	def test_get_absolute_url(self):
		self.assertEquals(self.category.get_absolute_url(), f'/{self.category.slug}/')


class PostModelTests(TestCase):
	
	@classmethod
	def setUpTestData(cls):
		image_path = 'D:\\ZProgramming\\Python\\dj\\myblog\\static\\test_image.jpg'
		new_image = SimpleUploadedFile(name = 'test_image.jpg',
												content = open(image_path, 'rb').read(), content_type = 'image/jpg')
		Category.objects.create(name = 'Test category name', slug = 'test-category-name')
		User.objects.create(username = 'shrrgn')
		Post.objects.create(title = 'Test Post title',
							slug = 'test-post-title',
							text = 'Test text test for Post model',
							image = new_image,
							user = User.objects.get(id = 1),
							category = Category.objects.get(id = 1))


	def setUp(self):
		self.post = Post.objects.get(id = 1)

	def test_post_creation(self):
		self.assertTrue(isinstance(self.post, Post))

	def test_post_title(self):
		field_label = self.post._meta.get_field('title').verbose_name
		
		self.assertEquals(field_label, 'title')
		self.assertEquals(self.post._meta.get_field('title').max_length, 100)
		self.assertEquals(self.post.title, 'Test Post title')

	def test_post_slug(self):
		field_label = self.post._meta.get_field('slug').verbose_name
		
		self.assertEquals(field_label, 'slug')
		self.assertIsNotNone(self.post.slug)
		self.assertEquals(self.post.slug, slugify(self.post.title))
		
	def test_post_text(self):
		field_label = self.post._meta.get_field('text').verbose_name
		
		self.assertEquals(field_label, 'text')
		self.assertEquals(self.post.text, 'Test text test for Post model')

	def test_post_date_published(self):
		field_label = self.post._meta.get_field('date_published').verbose_name
		now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")
		
		self.assertEquals(field_label, 'date_published'.replace('_', ' '))
		self.assertTrue(self.post._meta.get_field('date_published').auto_now_add)
		self.assertGreater(now, self.post.date_published.strftime("%Y-%m-%d %H:%M:%S:%f"))

	def test_post_image(self):
		field_label = self.post._meta.get_field('image').verbose_name
		self.assertEquals(field_label, 'image')
		#what i must do after i don't know----??????

	def test_post_likes(self):
		field_label = self.post._meta.get_field('likes').verbose_name
		
		self.assertEquals(field_label, 'likes')
		self.assertGreaterEqual(self.post.likes, 0)
		self.assertEquals(self.post._meta.get_field('likes').default, 0)

	def test_post_likes_adding(self):
		self.post.likes += 1
		self.assertEquals(self.post.likes, 1)

	def test_post_dislikes(self):
		field_label = self.post._meta.get_field('dislikes').verbose_name
		
		self.assertEquals(field_label, 'dislikes')
		self.assertGreaterEqual(self.post.dislikes, 0)
		self.assertEquals(self.post._meta.get_field('dislikes').default, 0)

	def test_post_dislikes_adding(self):
		self.post.dislikes += 1
		self.assertEquals(self.post.dislikes, 1)

	def test_post_user(self):
		self.assertEquals(self.post.user.username, User.objects.get(id = 1).username)

	def test_post_category(self):
		self.assertEquals(self.post.category.name, Category.objects.get(id = 1).name)

	def test_post_ordering(self):
		new_post = Post.objects.create(title = 'Test Post title 2',
							user = User.objects.get(id = 1),
							category = Category.objects.get(id = 1))
		new_post_2 = Post.objects.create(title = 'Test Post title 3',
							user = User.objects.get(id = 1),
							category = Category.objects.get(id = 1))
		posts = Post.objects.all()
		sorted_posts = sorted([self.post, new_post_2, new_post], key = lambda x: x.date_published, reverse = True)
		
		for i in range(len(posts) - 1):
			self.assertEquals(posts[i].title, sorted_posts[i].title)

	def test_post_reaction(self):
		field_label = self.post._meta.get_field('reaction').verbose_name
		
		self.assertEquals(field_label, 'reaction')
		self.assertTrue(self.post._meta.get_field('reaction').blank)
		
	def test_post_reaction_functionality(self):
		User.objects.create(username = 'poko')
		User.objects.create(username = 'test')
		self.post.reaction.add(User.objects.get(id = 1))
		self.post.reaction.add(User.objects.get(id = 2))

		self.assertIn(User.objects.get(id = 1), self.post.reaction.all())
		self.assertNotIn(User.objects.get(id = 3), self.post.reaction.all())
	
	def test_post_comments(self):
		pass		

	def test_post_str_method(self):
		self.assertEquals(self.post.title, str(self.post))

	def test_post_text_preview(self):
		self.assertEquals(self.post.text_preview(), self.post.text[:300] + "...")

	def test_post_absolute_url(self):
		self.category = Category.objects.get(id = 1)
		self.assertEquals(self.post.get_absolute_url(), f"/{self.category.slug}/{self.post.slug}/")

	def test_something(self):
		print('+==wow==+')