from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.
def register_view(request):
    """
    View function to render the user registration page.
    """
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request,form.save())
            return redirect("posts:list")
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form})  # Render the 'register.html' template in the 'user' directory
def login_view(request):
    """
    View function to render the user login page.
    """
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # If the form is valid, log in the user
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("posts:list")
            # Redirect to the posts list page after successful login
    else:
        form = AuthenticationForm()        
    return render(request, 'users/login.html',{'form': form})  # Render the 'login.html' template in the 'user' directory
def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect("posts:list")