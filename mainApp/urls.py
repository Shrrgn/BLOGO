from django.urls import path, include, re_path
from mainApp.views import CategoryListView
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('', CategoryListView.as_view(), name = 'wrapper'),
]