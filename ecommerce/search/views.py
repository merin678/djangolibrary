from django.shortcuts import render

# Create your views here.
from shop.models import Product
from django.db.models import Q
def search_products(request):
    k = None
    query = None
    if (request.method == "POST"):
        query = request.POST['q']  #get the input key from form
        if query:
            p= Product.objects.filter(

                Q(name__icontains=query) | Q(desc__icontains=query)

            )  #it checks the key in title and auther field in every records
            #if found then filters and return that record
            print(k)
    return render(request, 'search.html', {'product': p,'query': query})