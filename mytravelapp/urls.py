from . import views
from django.urls import path



urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('details/',views.details,name='details'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('thanks/',views.thanks,name='thanks'),
    path('demo/',views.demo,name='demo'),
    path('demo/add/',views.addition,name='addition')

]