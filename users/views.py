from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm

def index(request):
  if not request.user.is_authenticated:
    return HttpResponseRedirect(reverse("login"))
  return render(request, "users/user.html")
  
def login_view(request):
    
    if request.method == "POST":
      username = request.POST["username"]
      password = request.POST["password"]
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
      else:
        return render(request, "users/login.html",{
          "message" : "username or password is wrong"
        })
    return render(request, "users/login.html")



def logout_view(request):
  logout(request)
  return render(request, "users/login.html",{
    "message" : "logedout"

  })
def sign_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = CustomUserCreationForm()
    return render(request, "users/sign.html", {'form': form})


  #if request.method=="POST":
    username = request.POST["username"]
    password = request.POST["password"]
    email = request.POST["email"]
    user = User.objects.create_user(username, email , password)
    user.save()
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "users/login.html",{
          "message" : "username or password is wrong"
        })
    

      
    return HttpResponseRedirect(reverse("index"))

  #return render(request, "users/sign.html")"""

