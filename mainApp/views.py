from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from mainApp.models import Category, Post

# Create your views here.


class CategoryListView(ListView):
		
	model = Category
	template_name = 'mainApp/wrapper.html'

	def get_context_data(self, *args, **kwargs):
		context = super(CategoryListView, self).get_context_data(*args, **kwargs)
		context['categories'] = self.model.objects.all()
		return context

class CategoryDetailView(DetailView):
	model = Category
	template_name = 'category_detail.html'

	def get_context_data(self, *args, **kwargs):
		context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
		context['categories'] = self.model.objects.all()
		context['category'] = self.get_object()
		return context

class PostListView(ListView):
	model = Post
	template_name = 'mainApp/posts.html'

	def get_context_data(self, *args, **kwargs):
		context = super(PostListView, self).get_context_data(*args, **kwargs)
		context['posts'] = self.model.objects.all()
		return context

class PostDetailView(DetailView):
	model = Post
	template_name = 'mainApp/post_detail.html'
	context_object_name = 'post_detail'

	def get_context_data(self, *args, **kwargs):
		context = super(PostDetailView, self).get_context_data(*args, **kwargs)
		context['post'] = self.get_object()
		return context

def contacts(request):
	return render(request, "mainApp/contacts.html", {'values':['Contact name: Harry Potter', 
																'Address: Hogwarts Castle',
																'Contact email: harrypotter@ukr.net']})