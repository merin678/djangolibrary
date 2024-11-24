from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from app1.models import Movie
# def home(request):
#     k=Movie.objects.all()
#     return render(request,'home.html',{'movie':k})

class home(ListView):
    model=Movie
    template_name="home.html"
    context_object_name="movie"

    #to get a perticular item
    #name__icontains:which filter the item with k
    # icontains,startswith are the lookups

    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(title__icontains="K")
    #     return queryset



    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(title="Kaathal")
    #     return queryset


    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(title__startswith="a")
    #     return queryset


    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(year__gt="2002")
    #     return queryset
    #

# get_context_data
#     def get_context_data(self):
#         context=super().get_context_data()
#         context['name']="meri"
#         return context

    # extra_context={'name':'meri','age':21}

# def add(request):
#     if(request.method=="POST"):
#         t = request.POST['title']
#         d = request.POST['description']
#         y = request.POST['year']
#         l = request.POST['language']
#         i = request.FILES.get('img')
#
#         m=Movie.objects.create(title=t,description=d,year=y,language=l,img=i)
#         m.save()
#         return home(request)
#     return render(request,'add.html')
class add(CreateView):
    model=Movie
    fields=['title','description','year','language','image']
    template_name="add.html"
    success_url=reverse_lazy('app1:home')

class edit(UpdateView):
    model=Movie
    fields=['title','description','year','language','image']
    template_name="add.html"
    success_url=reverse_lazy('app1:home')



# def detail(request,i):
#     k=Movie.objects.get(id=i)
#     return render(request,'detail.html',{'movie':k})

class detail(DetailView):
    model=Movie
    template_name='detail.html'
    context_object_name="movie"

# def delete(request,i):
#     k=Movie.objects.get(id=i)
#     k.delete()
#     return home(request)
class delete(DeleteView):
    template_name="delete.html"
    model=Movie
    success_url=reverse_lazy('app1:home')


# def edit(request,i):
#     k = Movie.objects.get(id=i)
#     if(request.method=="POST"):
#         k.title=request.POST['t']
#         k.description=request.POST['d']
#         k.year=request.POST['y']
#         k.language=request.POST['l']
#         if(request.FILES.get('i')==None):
#             k.save()
#         else:
#             k.img=request.FILES.get('i')
#         k.save()
#         # return home(request)
#     return render(request,'edit.html',{'movie':k})


