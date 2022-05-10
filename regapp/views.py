from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from .models import registration


# Create your views here.




def reg(request):


    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        age = request.POST['age']
        sex = request.POST['sex']
        religion = request.POST['religion']

        regs =registration.objects.create(firstname=firstname, lastname=lastname, age=age, sex=sex, religion=religion)
        regs.save();
        print('regs craeted')
        return redirect('/')


    else:
        
        return render ( request, 'reg.html' )
