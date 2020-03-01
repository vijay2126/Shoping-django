from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import User1
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . import forms
from django.contrib.auth import authenticate, login, logout
from .models import Product
from math import ceil




def index(request):

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    # print(params)

    return render(request,"temp.html",params)

def login1(request):
    if request.method=="POST":
        form = forms.login(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user==None:
                return HttpResponse("vijay")
            if user is not None:
                if user.is_active:
                    login(request, user)

                    state = "Logged in!"
                    log = True
                    return HttpResponseRedirect('/')
                else:
                    state = "Not registered user"

    else:
        form=forms.login()
    return render(request,"login.html",{'form':form})





def Register(request):
    if request.method=="POST":
        form = forms.Register_Form(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['Password1'],
                email=form.cleaned_data['email']
            )
            return  HttpResponseRedirect("/")
    else:
        form=forms.Register_Form()
    return render(request,"registration.html",{'form':form})


# this is for logout
def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/')


def productView(request,myid):
    product=Product.objects.filter(id=myid)
    same_product=Product.objects.filter(category=product[0].category)
    same_product={i for i in same_product if i.id!=myid}
    return render(request,'productView.html',{'product':product[0],'related':same_product})



def women_product(request):

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat,subcategory='women')
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    # print(params)

    return render(request,"temp.html",params)



def men_product(request):

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat,subcategory='mens')
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    # print(params)

    return render(request,"temp.html",params)
