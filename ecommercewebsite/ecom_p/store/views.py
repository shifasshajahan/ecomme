from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from.models import category,Product
# Create your views here.
def index(request):
    return render(request,'index.html')
login_required(login_url='login')
def collections(request):
    Category=category.objects.filter(status=0)
    return render(request,'collections.html',{"category":Category})


def loginn(request):
    if request.method=="POST":
       username=request.POST['username']
       password=request.POST['password']
       user=auth.authenticate(username=username,password=password)
       if user is not None:
           auth.login(request,user)
           return redirect('/')
       else:
           messages.info(request,"invalid login")
           return redirect('login')
        
        
    return render(request,'login.html')

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,"username already exists")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email taken")
            return redirect('register')
        else:
         user=User.objects.create_user(username=username,email=email,password=password)
         user.save();
        return redirect('/')
    else: 
     return render(request,'register.html')



def logout(request):
    auth.logout(request)
    return redirect('/')


def collectionsview(request,slug):
    if(category.objects.filter(slug=slug,status=0)):
        product=Product.objects.filter(category__slug=slug)
    else:
        messages.error(request,"no")
        return redirect('collections')
    return render(request,'product.html', {"product":product})