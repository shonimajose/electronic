from django.urls import path
from .import views

urlpatterns = [
      path("",views.index,name='index'),
      path('SignIn',views.SignIn,name='SignIn'),
      path('SignUp',views.SignUp,name='SignUp'),
      path("Signout",views.SignOut,name="SignOut"),
      path("AdminIndex",views.AdminIndex,name="AdminIndex"),
      path("log/<int:pk>",views.log,name="log"),
      path("activate/<int:pk>",views.activate,name="activate")
]