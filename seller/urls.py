from django.urls import path
from . import views

app_name = "seller"
urlpatterns = [
    path('sellerhome',views.sellerhome, name='home'),
    path('addproduct', views.addproduct,name="addproduct"),
    path('viewproduct', views.viewproduct,name='viewproduct'),
    path('updateproduct',views.updateproduct,name='updateproduct'),
    path('getproduct',views.getproduct,name='getproduct'),
    path('delete_product/<int:p_id>',views.delete_product, name='delete_product'),
    path('viewpage/<int:p_id>',views.viewpage,name = 'viewpage'),
    path('index',views.index,name='index'),
    path('number',views.number,name = 'number')
]