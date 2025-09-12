from django.shortcuts import render,redirect
from .models import User
# Create your views here.

def index(request):
    if request.method == 'POST':
        fname=request.POST.get('f_name')
        lname=request.POST.get('l_name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        
        User.objects.create(first_name= fname, last_name=lname,email=email,age=age)
        return redirect('/')
        
        
    data= {
        'users':User.objects.all()
    }

    return render(request,'index.html',data )