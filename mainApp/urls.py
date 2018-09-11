from django.urls import path, include, re_path
from mainApp.views import (CategoryListView, CategoryDetailView, 
							PostListView, PostDetailView, 
							CreateCommentView, LikeDislikeView,
							RegistrationView, ContactsView,
							LoginView, UserAccountView,
							AddArticleToFavorites)
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


urlpatterns = [
	path('contacts/', ContactsView.as_view(), name = 'contacts'),
	path('add_comment/', CreateCommentView.as_view(), name = 'add_comment'),
	path('like_dislike/', LikeDislikeView.as_view(), name = 'like_dislike'),
	path('registration/', RegistrationView.as_view(), name = 'registration'),
	path('login/', LoginView.as_view(), name = 'login_page'),
	path('u/<user>/', UserAccountView.as_view(), name = 'user_detail'),
	path('logout/', LogoutView.as_view(next_page = reverse_lazy('wrapper')), name = 'logout_action'),
	path('add_to_favorites/', AddArticleToFavorites.as_view(), name = 'add_to_favorites'),
	path('posts/', PostListView.as_view(), name = 'posts'),
	path('', CategoryListView.as_view(), name = 'wrapper'),

	path('<slug>/', CategoryDetailView.as_view(), name = 'category_detail'),
	path('<category>/<slug>/', PostDetailView.as_view(), name = 'post_detail'),

	
]