from django.urls import path
from . import views

urlpatterns = [
    path('',views.index ),
    path('csignup',views.customer_signup),
    path('cslogin',views.customer_login),
    path('ssignup',views.seller_signup),
    path('sslogin',views.seller_login)
]
