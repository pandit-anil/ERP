from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib import messages
from .forms import UserForm,LoginForm

class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            
            if user is not None:
                login(request, user)
                messages.info(request, " logged in successfully.")
                return redirect('home')  # Redirect to the home page or another page after successful login
            else:
                form.add_error(None, 'Invalid username or password')
                
        return render(request, 'account/login.html', {'form': form})
    
class RegisterView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'account/register.html',{'form': form})

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = form.save(commit=False)  
            user.is_active = False  # Set the user as inactive
            user.set_password(password)  # Hash the password
            user.save()
            return redirect('login')  # Redirect to the login page after registration
                
        return render(request, 'account/register.html', {'form': form})
    


class ForgetView(View): 
    def get(self, request):
        return render(request, 'account/forget.html')
    
def Logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login') 