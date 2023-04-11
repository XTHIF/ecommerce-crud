from django.urls import path
from . import views

app_name = "customer"
urlpatterns = [
    path('viewproduct', views.viewproduct,name='viewproduct'),
]