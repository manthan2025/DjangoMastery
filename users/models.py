from django.db import models

# Create your models here.
class UserProfile(models.Model):
    """
    Model to represent a user profile.
    """
    username = models.CharField(max_length=150, unique=True)  # Unique username for the user
    email = models.EmailField(unique=True)  # Unique email address for the user
    bio = models.TextField(blank=True)  # Optional biography for the user
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)  # Optional profile picture

    def __str__(self):
        return self.username  # Return the username when the object is printed
