from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from mainApp.models import Category, Post
from mainApp.forms import CommentForm
from django.views.generic.base import View
from django.http import JsonResponse

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
		context['post_comments'] = self.get_object().comments.all()
		context['form'] = CommentForm()
		return context

class CreateCommentView(View):

	template_name = 'post_detail.html'

	def post(self, request, *args, **kwargs): #posting comment; if i wanna get it than get *GET*
		post_detail_id = self.request.POST.get('post_detail_id')
		comment = self.request.POST.get('comment')
		post = Post.objects.get(id = post_detail_id)
		new_comment = post.comments.create(author = request.user, comment = comment)
		comment = [{'author':new_comment.author.username, 
					'comment': new_comment.comment, 
					'timestamp':new_comment.timestemap.strtime('%Y-%m-%d')}]

		return JsonResponse(comment, safe = False)

def contacts(request): # how to make it better?
	return render(request, "mainApp/contacts.html", {'values':['Contact name: Harry Potter', 
																'Address: Hogwarts Castle',
																'Contact email: harrypotter@ukr.net']})