# from django.http import HttpResponse
from django.shortcuts import render # the render() function serves as a shortcut to generate HTTP responses by combining a template and data

def home(request):
    # return HttpResponse("Welcome to the home page!")
    return render(request, 'home.html')  # Render the home.html template
def about(request):
    # return HttpResponse("This is the about page!")
    return render(request, 'about.html')  # Render the about.html template