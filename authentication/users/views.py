from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from.models import Posts
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
  
    if request.method == 'POST':
        note=request.POST['note']
        p = Posts(post=note , usern = request.user)
        p.save()
    context = {
        "user": request.user,
        "posts":Posts.objects.all()
    }   
    return render(request, "users/user.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "users/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {"message": "Logged out."})

def register(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, "users/login.html")
    else:
        form = UserCreationForm()

        args = {'form' :form}
        return render(request, "users/register.html",args)
