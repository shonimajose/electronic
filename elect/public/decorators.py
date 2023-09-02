from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.http import HttpResponse

def admin_only(view_func):
    def wrapper_func(request,*args,**kwargs):
        group =None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        if group ==None:
            return view_func(request,*args,**kwargs)
        if group =="customer":
            return view_func(request,*args,**kwargs)  
        if group =="merchant":
           return redirect('AdminIndex')
    return wrapper_func
