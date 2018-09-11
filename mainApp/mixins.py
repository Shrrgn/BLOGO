from django.views.generic.list import MultipleObjectMixin
from mainApp.models import Category

class CategoryListMixin(MultipleObjectMixin):

	def get_context_data(self, *args, **kwargs):
		context = {}
		context['categories'] = Category.objects.all()
		return context