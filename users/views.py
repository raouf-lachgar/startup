from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import Product
from .forms import ProductForm
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    products = Product.objects.all().order_by('-created_at')
    
    return render(request, "users/user.html", {'products': products})

def profile_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    user_products = Product.objects.filter(user=request.user).order_by('-created_at')
    
    return render(request, "users/profile.html", {'products': user_products})

def delete_product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if product.user != request.user:
        messages.error(request, "You do not have permission to delete this product.")
        return redirect('profile')
    
    product.delete()
    messages.success(request, "Product deleted successfully.")
    return redirect('profile')

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
def submit_product_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            messages.success(request, "Product submitted successfully!")
            return redirect('index')
        else:
            messages.error(request, "There was an error with your submission. Please check the form and try again.")
    else:
        form = ProductForm()
    
    return render(request, "users/submit_product.html", {'form': form})
def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'users/product_detail.html', {'product': product})
def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to profile page after editing
    else:
        form = ProductForm(instance=product)

    return render(request, 'users/edit_product.html', {'form': form, 'product': product})
