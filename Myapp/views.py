from django.shortcuts import render
from  .models import Service
#from  .models import Service2
#from  .models import Service3
# Create your views here.

def index(request):

    servs = Service.objects.all()


    return render(request, 'index.html', {'servs': servs}) #'serv2': serv2, 'serv3': serv3})

     



  

"""
    serv1 = Service()
    serv1.price = 57 
    serv1.img = 'cat_cat_face_cats_eyes.jpg'
    serv1.tag = 'Normal' 
    serv1.offer1 = False
    serv1.offer2 = False
    serv1.offer3 = False

    serv2 = Service()
    serv2.price = 102
    serv2.img = 'cat_cute_cat_cat_face.jpg'
    serv2.tag = 'Classic'
    serv2.offer1 = True
    serv2.offer2 = False
    serv2.offer3 = False

    serv3 = Service()
    serv3.price = 156
    serv3.img = 'cat_feline_sleeping_cat.jpg'
    serv3.tag = 'Exclusive'
    serv3.offer1 = True
    serv3.offer2 = True
    serv3.offer3 = False

    serv4 = Service()
    serv4.price = 180
    serv4.img = 'price-1.jpg'
    serv4.tag = 'Top nutch'
    serv4.offer1 = True
    serv4.offer2 = True
    serv4.offer3 = True

    servs =[serv1, serv2, serv3, serv4] """



  

   