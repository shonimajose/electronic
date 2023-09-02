from django.db import models
from django.db import models
from product.models import ProductDetails
from django.contrib.auth.models import User

class cart(models.Model):
    
    product = models.ForeignKey(ProductDetails,on_delete=models.CASCADE)
    numberfoitems =models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    
# Create your models here.
class PurchasedItems(models.Model):
    product = models.ForeignKey(ProductDetails,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    paymentstatus = models.BooleanField(default=False)
     
    

    
# Create your models here.
