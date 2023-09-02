from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from product.models import ProductDetails
from.models import cart,PurchasedItems

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import razorpay

razorpay_client = razorpay.Client(auth =(settings.RAZOR_KEY_ID,settings.RAZOR_KEY_SECRET))     

@login_required(login_url="SignIn")
def CartView(request):
    product =cart.objects.filter(user = request.user)
    total=0
    for item in product:
        total = total + item.product.product_price
        
    context = {
       "products":product,
       "total":total,     
       
    }
    return render(request,'Cart.html',context)

@login_required(login_url="SignIn")
def AddCart(request,pk):
    product=ProductDetails.objects.get(productId = pk)
    Cartitem = cart.objects.create(product = product,numberfoitems = 1,user = request.user)
    Cartitem.save()
    return redirect("CartView")

def deletecart(request,pk):
    product =cart.objects.get(id = pk)
    product.delete()
    return redirect("CartView")

def Placeorder(request):
    products = cart.objects.filter(user = request.user)
    for i in products:
        product = i.product
        pitem = PurchasedItems.objects.create(product = product,user = request.user)
        pitem.save()
        i.delete()
        
    products = PurchasedItems.objects.filter(user = request.user,paymentstatus = False)  
    total = 0
    for items in products:
       total = total + items.product.product_price
   
   
    currency = 'INR'
    amount = total *100
    razorpay_order = razorpay_client.order.create(dict(amount=amount,currency =currency,payment_capture ="0"))
    razorpay_order_Id = razorpay_order["id"]
    callback_url ='paymenthandler/' 
    
    context = {     
            
    "razorpay_order_id":razorpay_order_Id,
    "razorpay_merchant_key":settings.RAZOR_KEY_ID,
    "razorpay_amount":amount,
    'currency':currency,
    'currency_url':callback_url,
    'slotid':"1"   
}    
    return render(request,"payment.html",context)
   
@csrf_exempt
def paymenthandler(request):
    if request.method == "POST":
        try:
            payment_id = request.POST.get('razorpay_payment_id','')
            razorpay_order_id = request.POST.get("razorpay_order_id","")
            signature = request.POST.get('razorpay_signature','')
            params_dict ={
                "razorpay_order_id":razorpay_order_id,
                "razorpay_payment_id":payment_id,
                "razorpay_signature":signature
            }
            result = razorpay_client.utility.verify_payment_signature(params_dict)
            if result is not None:
                amount = 6000
                razorpay_client.payment.capture(payment_id,amount)
                return HttpResponse("paymet Done")
            else:
                return HttpResponse('Done')
        except:
            products = PurchasedItems.objects.filter(user = request.user,paymentstatus = False)  
            for i in products:
                i.paymentstatus = True
                i.save()
            return HttpResponse("not Done")
def Customerorder(request):
    products = PurchasedItems.objects.all()
    context = {
        "products":products
    }
    return render(request,"orders.html",context)
    
        
    
# Create your views here.

# Create your views here.
