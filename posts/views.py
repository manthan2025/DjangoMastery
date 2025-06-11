from django.shortcuts import render, redirect
from .models import Post  # Import the Post model to interact with the database
# from django.http import HttpResponse # Import HttpResponse to return simple HTTP responses
from django.contrib.auth.decorators import login_required
# Import login_required to restrict access to certain views
from . import forms  
# Create your views here.
def posts_list(request):
    posts=Post.objects.all().order_by('-date')
    # This view will render the post list template
    return render(request, 'posts/posts_list.html',{'posts': posts})  # Pass the posts to the template
def post_page(request, slug):
    # return HttpResponse(f"Post page for slug: {slug}")  # Placeholder response for the post page
    post=Post.objects.get(slug=slug)  # Retrieve the post with the given slug from the database
    return render(request, 'posts/post_page.html',{'post': post})
@login_required(login_url='/users/login/')  # Use the login_required decorator to restrict access to this view
def post_new(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('posts:list')
    # Placeholder for the new post creation view
    # In a real application, you would handle form submission and save the new post here
    else:
        form=forms.CreatePost()
    return render(request, 'posts/post_new.html', {'form': form})  # Render the 'post_new.html' template with the form