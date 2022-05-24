from django.urls import path

from . import views

urlpatterns = [
    path('', views.reg, name='reg'),
    path('showreg/', views.showreg, name='showreg'),
    path('updatereg/<str:firstname>', views.updatereg, name='updatereg'),
    path('deletereg/<str:firstname>', views.deletereg, name='deletereg'),
    ] 


    