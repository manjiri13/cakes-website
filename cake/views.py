from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def log(request):
    if request.user.is_anonymous:
        return redirect("https://google.com/")
    return render(request,"index1.html")
        # return redirect("/login")
    
def home(request):
    return render(request,"index.html")
def menu(request):
    products = Product.objects.all()
    context = {"products":products}
    return render(request,"menu.html",context)
def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items':items}
   
    return render(request,"cart.html",context)

def checkout(request):
    # forms1= cakeform()
    return render(request,"checkout.html")
def loginme(request):
    if request.method=="POST":
        username = request.POST.get['email']
        password = request.POST.get['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("https://google.com/")
        else:
            return render(request,"login.html")
    return render(request,"login.html")
def logoutme(request):
    logout(request)
    return redirect("https://google.com/")

def register(request):
    if request.method=="POST":
        name = request.POST.get['name']
        username = request.POST.get['email']
        password = request.POST.get['password']
        
        
        return render(request,"menu.html")

