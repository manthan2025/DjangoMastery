from django.urls import path
from . import views  # Import views from the current directory

app_name = 'posts'  # Define the app name for namespacing URLs
urlpatterns = [
    
    path('', views.posts_list, name='list'),  # URL for the home page can be added here
    path('new-post/', views.post_new, name='new-post'),  # URL for creating a new post
    path('<slug:slug>', views.post_page, name='page'), 
    path('post/<slug:slug>/comment/', views.add_comment, name='add_comment'),  # Add this line
    path('post/<slug:slug>/comment/<int:comment_id>/reply/', views.add_reply, name='add_reply'),
]