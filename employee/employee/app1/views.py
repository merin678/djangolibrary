from django.shortcuts import render
from app1.models import Employee

# Create your views here.
def home(request):
    k=Employee.objects.all()
    return render(request,'home.html',{'employee':k})

def add(request):
    if request.method=="POST":
        ename = request.POST.get('e')
        age = request.POST.get('a')
        address = request.POST.get('ad')
        email = request.POST.get('em')
        image = request.FILES.get('i', None)  # Use request.FILES for file upload

        e=Employee.objects.create(ename=ename,age=age,address=address,email=email,image=image)
        e.save()
        return home(request)
    return render(request,'add.html')

def detail(request,m):
    k=Employee.objects.get(id=m)
    return render(request,'detail.html',{'employee':k})

def edit(request,m):
    k=Employee.objects.get(id=m)
    if request.method == "POST":
        k.ename= request.POST['e']
        k.age = request.POST['a']
        k.address = request.POST['ad']
        k.email = request.POST['em']


        if request.FILES.get('i') == None:
            k.save()
        else:
            k.image = request.FILES.get('i')
        k.save()
        return home(request)
    return render(request,'edit.html',{'employee':k})

def delete(request,m):
    k=Employee.objects.get(id=m)
    k.delete()
    return home(request)