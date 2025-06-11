from django.contrib import admin
from .models import Post  # Import the Post model from the current directory
# Register your models here.
admin.site.register(Post)  # Register the Post model to make it available in the admin interface