from django.contrib import admin
from .models import Post, Comment, Reply  # Import the Post, Comment, and Reply models from the current directory

# Register your models here.
admin.site.register(Post)  # Register the Post model to make it available in the admin interface
admin.site.register(Comment)  # Register the Comment model to make it available in the admin interface
admin.site.register(Reply)  # Register the Reply model to make it available in the admin interface