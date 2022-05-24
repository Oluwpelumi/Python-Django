
from django.shortcuts import render, redirect
from regapp.forms import registrationform
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
        return render (request, 'reg.html')




def showreg(request):
    shows = registration.objects.all()
    return render(request, 'showreg.html', {'shows':shows})




def updatereg(request, firstname):
    regs = registration.objects.get(firstname=firstname)
    form = registrationform(request.POST, instance=regs)
    if form.is_valid():
        form.save();
        return redirect('/')
    else:
        return render(request, 'updatereg.html', {'regs':regs})




def deletereg(request, firstname):
    regss = registration.objects.get(firstname=firstname)
    regss.delete();
    return redirect('/')

