from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):
    data = {
        'dojos': Dojo.objects.all(),
        'ninjas': Ninja.objects.all()
    }

    return render(request, 'index.html',data)


def dojo(request):
    if request.method == 'POST':
        if request.POST['which_form']=='dojo':
            d_name= request.POST['d_name']
            city= request.POST['city']
            state= request.POST['state']
            Dojo.objects.create(name=d_name,city=city,state=state)

        elif request.POST['which_form']=='ninja':
            f_name= request.POST['f_name']
            l_name= request.POST['l_name']
            sdojo= request.POST['sdojo']  
            ssdojo=Dojo.objects.get(id=sdojo)
            Ninja.objects.create(f_name=f_name,l_name=l_name,dojo=ssdojo)
                     

    return redirect( '/')