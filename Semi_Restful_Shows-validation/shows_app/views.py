from django.shortcuts import render,redirect
from .models import Show
from django.contrib import messages 
# Create your views here.

def index(request):
    return redirect('/shows/')


def shows(request): 
    data={
        'shows': Show.objects.all()
    }
    return render(request, 'shows.html',data)


def show_num(request,num):
    data={
        'show': Show.objects.get(id=num)
    }
    return render(request, 'show.html',data)


def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method =='POST':
        error=Show.objects.validaterShow(request.POST)
        if len(error)>0:
            for key,value in error.items():
              messages.error(request,value)
            return redirect('new')
            
        title = request.POST['title']
        network= request.POST['network']
        r_date= request.POST['r_date']
        desc= request.POST['desc']
        Show.objects.create(title=title,network=network,release_date=r_date, description=desc)
    

    
    return redirect('/shows/')


def edit(request,num):
    show = Show.objects.get(id=num)
    return render (request, 'edit.html',{'show':show})


def update(request,num):
    if request.method =='POST':
        error=Show.objects.validaterShow(request.POST)
        if len(error)>0:
            for key,value in error.items():
              messages.error(request,value)
            return redirect('edit',num=num)
                    
        
        
        updated = Show.objects.get(id=num)
        updated.title = request.POST['title']
        updated.network= request.POST['network']
        updated.release_date= request.POST['r_date']
        updated.description= request.POST['desc']
        updated.save()
        
    return redirect('/shows/',num=updated.id)


def delete(request,num):
    show_d = Show.objects.get(id=num)
    show_d.delete()
    return redirect('/shows/')