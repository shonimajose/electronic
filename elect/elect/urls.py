
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

from public import views
from public import urls
import public  
from product import urls
import product 
from Cart import views,urls
import Cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(public.urls)),
    path("product/",include(product.urls)),
    path("Cart/",include(Cart.urls)),
    

]
urlpatterns =urlpatterns + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)