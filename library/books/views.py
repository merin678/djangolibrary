from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from books.models import Book


# Create your views here.


def home(request):
    context = {'name': 'merin', 'age': 22}
    return render(request, 'home.html', context)


@login_required
def add_book(request):
    if (request.method == "POST"):
        t = request.POST['t']
        a = request.POST['a']
        pg = request.POST['pg']
        pr = request.POST['pr']
        l = request.POST['l']
        c = request.FILES['i']
        f = request.FILES['f']

        b = Book.objects.create(title=t, author=a, pages=pg, price=pr, language=l, cover=c, pdf=f)  #create a new record
        b.save()  #saves the record inside table
        return view_book(request)

    return render(request, 'add.html')


@login_required
def view_book(request):
    k = Book.objects.all()  #read all the records from table Book and assign it to k
    return render(request, 'view.html', {'book': k})


@login_required
def detail(request, i):
    k = Book.objects.get(id=i)
    return render(request, 'detail.html', {'book': k})


@login_required
def edit(request, i):
    k = Book.objects.get(id=i)
    if (request.method == "POST"):
        k.title = request.POST['t']
        k.author = request.POST['a']
        k.pages = request.POST['pg']
        k.price = request.POST['pr']
        k.language = request.POST['l']

        if request.FILES.get('i') == None:
            k.save()
        else:
            k.cover = request.FILES['i']

        if request.FILES.get('f') == None:
            k.save()
        else:
            k.pdf = request.FILES['f']
        k.save()
        return view_book(request)

    return render(request, 'edit.html', {'book': k})


@login_required
def delete(request, i):
    k = Book.objects.get(id=i)
    k.delete()
    return view_book(request)


from django.db.models import Q

def search(request):
    k = None
    query = None
    if (request.method == "POST"):
        query = request.POST['q']  #get the input key from form
        if query:
            k = Book.objects.filter(

                Q(title__icontains=query) | Q(author__icontains=query)

            )  #it checks the key in title and auther field in every records
            #if found then filters and return that record
            print(k)
    return render(request, 'search.html', {'book': k,'query': query})
