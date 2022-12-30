
from django.urls import path, include

from ecommerce import settings
from django.conf.urls.static import static
from django.urls import path
from myapp import views
app_name='myapp'
urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='productsCatdetail')
]