from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from mainApp.models import Category, Post, UserAccount
from mainApp.forms import CommentForm, RegisrationForm, LoginForm
from django.views.generic.base import View
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model, authenticate, login, logout

# Create your views here.

User = get_user_model()

class CategoryListView(ListView):
		
	model = Category
	template_name = 'mainApp/wrapper.html'

	def get_context_data(self, *args, **kwargs):
		context = super(CategoryListView, self).get_context_data(*args, **kwargs)
		context['categories'] = self.model.objects.all()
		return context

class CategoryDetailView(DetailView):
	model = Category
	template_name = 'mainApp/category_detail.html' # url((

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
		print(f"{self.request.user} {self.request.user.is_anonymous}")
		
		if not self.request.user.is_anonymous:
			context['current_user'] = UserAccount.objects.get(nick = self.request.user)

		return context

class CreateCommentView(View):

	template_name = 'mainApp/post_detail.html'

	def post(self, request, *args, **kwargs): #posting comment; if i wanna get it than get *GET*
		post_detail_id = self.request.POST.get('post_detail_id')
		comment = self.request.POST.get('comment')
		post = Post.objects.get(id = post_detail_id)
		new_comment = post.comments.create(author = request.user, comment = comment)
		comment = [{'author':new_comment.author.username, 
					'comment': new_comment.comment, 
					'timestamp':new_comment.timestemap.strtime('%Y-%m-%d')}]

		return JsonResponse(comment, safe = False)

class LikeDislikeView(View):

	template_name = 'mainApp/post_detail.html'

	def get(self, request, *args, **kwargs):
		post_detail_id = self.request.GET.get('post_detail_id')
		post = Post.objects.get(id = post_detail_id)
		like = self.request.GET.get('like')
		dislike = self.request.GET.get('dislike')
		
		if like and (request.user not in post.reaction.all()):
			post.likes += 1 
			post.reaction.add(request.user)
			post.save()
		
		if dislike and (request.user not in post.reaction.all()):
			post.dislikes += 1 
			post.reaction.add(request.user)
			post.save()
		
		data = {
			'like':post.likes,
			'dislike':post.dislikes 
		}

		return JsonResponse(data)
		
class RegistrationView(View):

	template_name = 'mainApp/registration.html'

	def get(self, request, *args, **kwargs):
		form = RegisrationForm(request.POST or None)
		context = {'form':form}
		return render(self.request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		form = RegisrationForm(request.POST or None)
		
		if form.is_valid():
			new_user = form.save(commit = False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			password_check = form.cleaned_data['password_check']
			new_user.set_password(password)
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			new_user.save()
			UserAccount.objects.create(nick = User.objects.get(username = new_user.username),
										first_name = new_user.first_name,
										last_name = new_user.last_name,
										email = new_user.email)
		
			return HttpResponseRedirect('/')

		context = {'form':form}
		return render(self.request, self.template_name, context)

class LoginView(View):

	template_name = 'mainApp/login.html'

	def get(self, request, *args, **kwargs):
		form = LoginForm()
		context = {'form':form}
		return render(self.request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		form = LoginForm(request.POST or None)
		
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username = username, password = password)

			if user:
				login(self.request, user) 
				return HttpResponseRedirect('/')

		context = {'form':form}
		return render(self.request, self.template_name, context)


class UserAccountView(View):

	template_name = 'mainApp/user_detail.html'

	def get(self, request, *args, **kwargs):
		user = self.kwargs.get('user')
		current_user = UserAccount.objects.get(nick = User.objects.get(username = user))
		print(current_user.email)
		context = {'current_user':current_user}
		return render(self.request, self.template_name, context)


class ContactsView(View):

	template_name = "mainApp/contacts.html"

	def get(self, request, *args, **kwargs):
		context = {
			'name':'Harry Potter',
			'address':'Hogwarts Castle',
			'email':'harrypotter@ukr.net'
		}
		return render(self.request, self.template_name, context)
																
