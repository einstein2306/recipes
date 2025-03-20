from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from .models import Recipe
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your views here.

def register(request):
    if request.method == "POST":

        # retrieve the values from the form..
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]

        user = User.objects.create_user(username=username,
                                        email=email,
                                        password=password,
                                        first_name=firstName,
                                        last_name=lastName 
                                    )
        user.save()
        login(request,user)
        r = Recipe.objects.filter(user=user)
        return render(request,"recipe/home.html",{
            "recipes":r,
            "user":user,
            'STATIC_VERSION': now().timestamp(),  # Cache-busting version
        })

    return render(request,"recipe/register.html",{
        'STATIC_VERSION': now().timestamp(),  # Cache-busting version
    })

def index(request):
    
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    r = Recipe.objects.filter(user=request.user)
    return render(request,"recipe/home.html",{
        "recipes":r,
        "user":request.user,
        'STATIC_VERSION': now().timestamp(),  # Cache-busting version
    })
    
def login_view(request):
    if request.method == "POST":

        # retrieve the data from the form..
        username = request.POST["username"]
        password = request.POST["password"]

        # check the user..
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        
        else:
            return render(request,"recipe/login.html",{
                "message":"Invalid Credentials.",
                'STATIC_VERSION': now().timestamp(),  # Cache-busting version
            })
   
    return render(request,"recipe/login.html",{
        'STATIC_VERSION': now().timestamp(),  # Cache-busting version
    })
        

def logout_view(request):
    logout(request)
    return render(request,"recipe/login.html",{
        "message":"Successfully Logged out.",
        'STATIC_VERSION': now().timestamp(),  # Cache-busting version
    })

def add_item(request):
    if request.method == "POST":

        title = request.POST["item"]
        ingredients = request.POST["ingredients"]
        process = request.POST["process"]

        create_recipe = Recipe(user=request.user,title=title,ingredients=ingredients,process=process)
        create_recipe.save()
        return HttpResponseRedirect(reverse('index'))
    
    return render(request,"recipe/add_item.html",{
        'STATIC_VERSION': now().timestamp(),  # Cache-busting version
    })

def show_process(request,process):
    return render(request,"recipe/process.html",{
        "process":process,
        'STATIC_VERSION': now().timestamp(),  # Cache-busting version
    })






