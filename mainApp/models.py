from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length = 20, unique = True)
	slug = models.SlugField()

	def __str__(self):
		return self.name

	def get_abdolute_url(self):
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

	class Meta:
		ordering = ["-date_published"]

	def __str__(self):
		return self.title

	def text_preview(self):
		return self.text[:300] + '...'

	def get_abdolute_url(self):
		return reverse('post_detail', kwargs = {'slug' :self.slug})


