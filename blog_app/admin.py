from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish', 'author', 'publish', 'status']
