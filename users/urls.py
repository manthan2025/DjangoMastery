from django.urls import path
from . import views  # Import views from the current directory

app_name = 'users'  # Define the app name for namespacing URLs
urlpatterns = [
    path('register/', views.register_view, name='register'),  # URL for the home page can be added here 
    path('login/', views.login_view, name='login'),  # URL for the about page can be added here
    path('logout/', views.logout_view, name='logout'),  # URL for the logout page
]