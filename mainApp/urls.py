from django.urls import path, include, re_path
from mainApp.views import (CategoryListView, CategoryDetailView, 
							PostListView, PostDetailView, 
							CreateCommentView, LikeDislikeView,
							RegistrationView, ContactsView)


urlpatterns = [
	#re_path('/category/(?P<slug>[-\w]+)/', CategoryDetailView.as_view(), name = 'category_detail'), #fuck!
	path('', CategoryListView.as_view(), name = 'wrapper'),
	path('posts/', PostListView.as_view(), name = 'posts'),
	path('/category/post/(?P<slug>[-\w]+)/', PostDetailView.as_view(), name = 'post_detail'),
	path('contacts/', ContactsView.as_view(), name = 'contacts'),
	path('add_comment/', CreateCommentView.as_view(), name = 'add_comment'),
	path('like_dislike/', LikeDislikeView.as_view(), name = 'like_dislike'),
	path('registration/', RegistrationView.as_view(), name = 'registration')
]