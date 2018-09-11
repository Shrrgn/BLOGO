from django.urls import path, include, re_path
from mainApp.views import (CategoryListView, CategoryDetailView, 
							PostListView, PostDetailView, 
							CreateCommentView, LikeDislikeView,
							RegistrationView, ContactsView,
							LoginView, UserAccountView)
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


urlpatterns = [
	#re_path('/category/(?P<slug>[-\w]+)/', CategoryDetailView.as_view(), name = 'category_detail'), #fuck!
	path('', CategoryListView.as_view(), name = 'wrapper'),
	path('posts/', PostListView.as_view(), name = 'posts'),
	path('/category/post/(?P<slug>[-\w]+)/', PostDetailView.as_view(), name = 'post_detail'),
	path('contacts/', ContactsView.as_view(), name = 'contacts'),
	path('add_comment/', CreateCommentView.as_view(), name = 'add_comment'),
	path('like_dislike/', LikeDislikeView.as_view(), name = 'like_dislike'),
	path('registration/', RegistrationView.as_view(), name = 'registration'),
	path('login/', LoginView.as_view(), name = 'login_page'),
	path('u/(?P<user>[-\w]+)/', UserAccountView.as_view(), name = 'user_detail'),
	path('logout/', LogoutView.as_view(next_page = reverse_lazy('wrapper')), name = 'logout_action'),
]