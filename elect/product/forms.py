from django.forms import ModelForm
from .models import ProductDetails

class productAddform(ModelForm):
    class Meta:
        model =ProductDetails
        fields =["product_Name","product_Brand","product_Discription","product_price","product_category","product_stock","product_image"]