from django.shortcuts import render
from django.views.generic.list import ListView
from mainApp.models import Category

# Create your views here.

def index(request):
	return render(request, "mainApp/mainPage.html")


class CategoryListView(ListView):
		
	model = Category
	template_name = 'mainApp/wrapper.html'

	def get_context_data(self, *args, **kwargs):
		context = super(CategoryListView, self).get_context_data(*args, **kwargs)
		context['categories'] = self.model.objects.all()
		return context