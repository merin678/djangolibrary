from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

# Create your views here.
from shop.models import Category,Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse
def allcategories(request):
    c=Category.objects.all()
    context={'cat':c}
    return render(request,'category.html',context)
def allproducts(request,id):
    c = Category.objects.get(id=id)
    p=Product.objects.filter(category=c)
    context={'cat':c,'product':p}
    return render(request,'product.html',context)

def details(request,id):
    d=Product.objects.filter(id=id)
    return render(request, 'details.html',{'product':d})

def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        if(p==cp):
            u=User.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e)
            u.save()
        else:
            return HttpResponse("passwords doesn't match")
        return redirect('shop:login')
    return render(request, 'register.html')


def login(request):
    if(request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            auth_login(request,user)
            return redirect('shop:categories')
        else:
            return HttpResponse("Invalid username or password.")
    return render(request, 'login.html')
@login_required
def logout(request):
    auth_logout(request)
    return redirect('shop:login')


def home(request):
    return login(request)

def add_category(request):
    if(request.method == "POST"):
        n=request.POST['n']
        i=request.FILES.get('i')
        d=request.POST['desc']
        c=Category.objects.create(name=n,image=i,desc=d)
        c.save()
    return render(request, 'add_category.html')

def add_product(request):
    if(request.method == "POST"):
        n=request.POST['n']
        i=request.POST['i']
        d=request.POST['d']
        s=request.POST['s']
        p=request.POST['p']
        c=request.POST['c']
        cat=Category.objects.get(name=c) #category object/record matching with category name c

        p=Product.objects.create(name=n,image=i,desc=d,stock=s,price=p,category=cat)
        p.save()
        return redirect('shop:categories')
    return render(request, 'add_product.html')

def add_stock(request,p):
    product=Product.objects.get(id=p)
    if(request.method=="POST"):
        product.stock=request.POST['n']
        product.save()
        return redirect('shop:categories')
    context={'pro':product}
    return render(request, 'add_stock.html',context)
