from django.urls import path, include, re_path
from mainApp.views import CategoryListView, CategoryDetailView, PostListView, PostDetailView
from . import views

urlpatterns = [
	#re_path('/category/(?P<slug>[-\w]+)/', CategoryDetailView.as_view(), name = 'category_detail'), #fuck!
	path('', CategoryListView.as_view(), name = 'wrapper'),
	path('posts/', PostListView.as_view(), name = 'posts'),
	path('/category/post/(?P<slug>[-\w]+)/', PostDetailView.as_view(), name = 'post_detail'),
	path('contacts/', views.contacts, name = 'contacts')
]