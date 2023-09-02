from django.db import models
from django.contrib.auth.models import User

class ProductDetails(models.Model):
    
    option =(
        ("Laptops","Laptops"),
        ("Mobiles","Mobiles"),
        ("Camera","Camera"),
        ("Others","Others")
        )

    productId = models.AutoField(primary_key=True)
    product_Name = models.CharField(max_length=255)
    product_Brand = models.CharField(max_length=255)
    product_Discription = models.CharField(max_length=1000)
    product_price = models.IntegerField()
    product_category=models.CharField(max_length=255,choices=option)
    product_image = models.ImageField(upload_to="product_image")
    product_stock=models.PositiveIntegerField()
    merchant = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    

