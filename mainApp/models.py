from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

# Create your models here.

class Category(models.Model):
	
	name = models.CharField(max_length = 20, unique = True)
	slug = models.SlugField()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('category_detail', kwargs = {'slug' :self.slug})


def generate_filename(instance, filename):
	filename = instance.slug + '.jpg'
	return f"{instance}/{filename}"

class Post(models.Model):
	
	title = models.CharField(max_length = 100)
	date_published = models.DateTimeField(auto_now_add = True)
	slug = models.SlugField()
	text = models.TextField()
	image = models.ImageField(upload_to = generate_filename)
	likes = models.PositiveIntegerField(default = 0)
	dislikes = models.PositiveIntegerField(default = 0)
	user = models.ForeignKey('auth.User', on_delete = models.CASCADE)
	category = models.ForeignKey('Category', on_delete = models.CASCADE)
	comments = GenericRelation('comments')
	reaction = models.ManyToManyField('auth.User', blank = True, related_name = 'user_reaction_for_post')

	class Meta:
		ordering = ["-date_published"]

	def __str__(self):
		return self.title

	def text_preview(self):
		return self.text[:300] + '...'

	def get_absolute_url(self):
		return reverse('post_detail', kwargs = {'slug':self.slug, 'category':self.category.slug})

	#def __eq__(self, other):
	#	return self.title == other.title and self.text == other.text

class Comments(models.Model):
	
	author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
	comment = models.CharField(max_length = 140)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)

	object_id = models.PositiveIntegerField()
	content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE)
	content_object = GenericForeignKey('content_type', 'object_id')

class UserAccount(models.Model):

	nick = models.OneToOneField('auth.User', on_delete = models.CASCADE)
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 30)
	email = models.EmailField()
	favorite_posts = models.ManyToManyField(Post)

	def __str__(self):
		return self.nick.username

	def full_name(self):
		return f"{self.first_name} {self.last_name}"

	def get_absolute_url(self): #for difficult url
		return reverse('user_detail', kwargs = {'user':self.nick.username})
