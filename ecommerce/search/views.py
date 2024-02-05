from django.shortcuts import render
from shop.models import Products
from django.db.models import Q
def search(request):
    query=""
    b=None
    if(request.method=='POST'):
        query=request.POST['q']
        if(query):
            b=Products.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))

    return render(request,template_name='search.html',context={'query':query,'b':b})
