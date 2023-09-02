from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserAddForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .decorators import admin_only
from product.models import ProductDetails
from django.template.loader import render_to_string  

from django.core.mail import send_mail
from django.conf import settings


@admin_only
def index(request):
    Product = ProductDetails.objects.all()
    
    context ={
        "product":Product
    }
    return render(request,'index.html',context)

def AdminIndex(request):
    return render(request,"adminhome.html")
    
def SignIn(request):
    if request.method == "POST":
        username = request.POST["uname"]
        password = request.POST["pswd"]
        user = authenticate(request,username = username,password =password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,"username or password incorrect")
            return redirect('SignIn')

    return render(request,'login.html')

def SignUp(request):
    form = UserAddForm()
    if request.method =="POST":
        form = UserAddForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")

            if User.objects.filter(username = username).exists():
                messages.info(request,"User Name Already exists")
                return redirect('SignUp')
            else:
                user = form.save(commit=False)  
                user.is_active = False  
                user.save()
                message = render_to_string('email.html', {
                    'user': user,
                    'pk':user.id,  
                 
                })  

                send_mail(
                    'hy',
                    message,
                    'settings.EMAIL_HOST_USER', 
                    [email] )
                messages.success(request,"User Created")
                pk=user.id
                return redirect('log',pk)
            

    context = {"form":form}
    return render(request,'register.html',context)



def SignOut(request):
    logout(request)
    return redirect('index')

def log(request,pk):
    user=User.objects.get(id=pk)
    check=user.is_active
    context ={
        'check':check
    }

    return render(request,'log.html',context)

def activate(request,pk):
    user=User.objects.get(id=pk)
    user.is_active = True
    user.save()  

    return redirect('SignIn')
# Create your views here.
