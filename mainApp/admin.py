from django.contrib import admin
from mainApp.models import Category, Post, Comments, UserAccount


class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comments)
admin.site.register(UserAccount)