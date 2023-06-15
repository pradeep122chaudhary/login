from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

# from django.contrib.auth import logout
# from django.contrib.auth.views import logout
from django.http import HttpResponse
from .forms import EmailMobileUserForm
# Create your views here.

@login_required
def home(request): 
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request,"index.html")

@login_required
def dashboard(request):
    print(request.user)
    return render(request,"done.html")

def logout(request):
        # logout(request)
       # auth_logout(request)
        return redirect("home")
     
    