from django.shortcuts import render
from shop.models import Category,Products
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
def allcategories(request):
    b=Category.objects.all()
    return render(request,'category.html',{'b':b})

def product(request,p):
    b=Category.objects.get(name=p)
    p=Products.objects.filter(category=b)
    return render(request,'product.html',{'b':b,'p':p})

def detail(request,p):
    b=Products.objects.get(name=p)
    return render(request,'detail.html',{'b':b})

def register(request):
    if(request.method=='POST'):
        u=request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        if(p==cp):
            user = User.objects.create_user(username=u, password=p, first_name=f,last_name=l, email=e)
            user.save()
            return allcategories(request)
        else:
            return HttpResponse("Passwords doesn't match")
    return render(request,'register.html')

def user_login(request):
    if (request.method == 'POST'):
        u = request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u,password=p)
        if(user):
            login(request,user)
            return allcategories(request)
        else:
            return HttpResponse("Invalid Credentials")
    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return allcategories(request)