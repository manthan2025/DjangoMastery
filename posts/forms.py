from django import forms
from . import models

class CreatePost(forms.ModelForm):
    """
    Form to create a new post.
    """
    class Meta:
        model = models.Post  # Specify the model to use for this form
        fields = ['title', 'content','slug','banner']  # Fields to include in the form
