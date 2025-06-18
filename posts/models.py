from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)  # Title of the post
    content = models.TextField()  # Content of the post
    slug= models.SlugField(unique=True)  # Unique slug for the post, used in URLs
    author = models.ForeignKey(User,on_delete=models.CASCADE, default=None)  # Author of the post
    date= models.DateTimeField(auto_now_add=True)  # Date when the post was created
    banner = models.ImageField(default='fallback.jpg',blank=True)  # Optional banner image for the post
    def __str__(self):
        return self.title  # Return the title of the post when the object is printed

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']  # Newest comments first

    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'


class Reply(models.Model):
    comment = models.ForeignKey('Comment', related_name='replies', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']