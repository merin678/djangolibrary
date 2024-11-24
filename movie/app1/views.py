from django.shortcuts import render

# Create your views here.
from app1.models import Movie
def home(request):
    k=Movie.objects.all()
    return render(request,'home.html',{'movie':k})

def add(request):
    if(request.method=="POST"):
        t = request.POST['title']
        d = request.POST['description']
        y = request.POST['year']
        l = request.POST['language']
        i = request.FILES.get('image')

        m=Movie.objects.create(title=t,description=d,year=y,language=l,image=i)
        m.save()
        return home(request)
    return render(request,'add.html')

def detail(request,i):
    k=Movie.objects.get(id=i)
    return render(request,'detail.html',{'movie':k})

def delete(request,i):
    k=Movie.objects.get(id=i)
    k.delete()
    return home(request)

def edit(request,i):
    k = Movie.objects.get(id=i)
    if(request.method=="POST"):
        k.title=request.POST['t']
        k.description=request.POST['d']
        k.year=request.POST['y']
        k.language=request.POST['l']
        if(request.FILES.get('i')==None):
            k.save()
        else:
            k.image=request.FILES.get('i')
        k.save()
        # return home(request)
    return render(request,'edit.html',{'movie':k})