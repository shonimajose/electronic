from django.urls import path
from.import views

urlpatterns = [
    path("CartView",views.CartView,name="CartView"),
    path("AddCart/<int:pk>",views.AddCart,name="AddCart"),
    path("deletecart/<int:pk>",views.deletecart,name="deletecart"),
    path("Placeorder",views.Placeorder,name="Placeorder"),
    path("paymenthandler",views.paymenthandler,name="paymenthandler"),
    path("Customerorder",views.Customerorder,name="Customerorder")
    
]
