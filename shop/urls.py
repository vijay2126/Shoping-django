from django.contrib import admin
from django.urls import path,include
from . import views;

app_name = 'shop'

urlpatterns = [
    path("",views.index, name='index'),
    path("register", views.Register, name='register'),
    path("login1", views.login1, name='login'),
    path("logout_user", views.logout_user, name='logout'),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("women", views.women_product, name="women"),
    path("men", views.men_product, name="men"),

]
