from django.shortcuts import render
from movie.models import Movie
from movie.forms import Movieform

def addmovie(request):
    if(request.method=='POST'):
        form=Movieform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return viewmovie(request)
    form=Movieform()
    return render(request,template_name='addmovie.html',context={'form':form})

def viewmovie(request):
    b=Movie.objects.all()
    return render(request,template_name='viewmovie.html',context={'b':b})

def detail(request,p):
    b=Movie.objects.get(name=p)
    return render(request,template_name='detail.html',context={'b':b})

def delete(request,p):
    b=Movie.objects.get(name=p)
    b.delete()
    return viewmovie(request)

def update(request,p):
    b = Movie.objects.get(name=p)
    if (request.method == 'POST'):
        form = Movieform(request.POST,request.FILES,instance=b)
        if form.is_valid():
            form.save()
            return viewmovie(request)

    form=Movieform(instance=b)
    return render(request,template_name='update.html',context={'form':form})
