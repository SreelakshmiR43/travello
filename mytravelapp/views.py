from django.http import HttpResponse
from django.shortcuts import render
from .models import place, team


# Create your views here.
def index(request):
    obj = place.objects.all()
    obj1 = team.objects.all()
    return render(request, 'index.html',{'result':obj,'res':obj1})


def home(request):
    return HttpResponse("Hello ,this is the Home page")


def details(request):
    return render(request, 'details.html')


def about(request):
    return render(request, 'aboutus.html')


def contact(request):
    return render(request, 'contact.html')


def thanks(request):
    return render(request, 'thanks.html')


def demo(request):
    name = "India"
    return render(request, 'demo.html', {'obj': name})


def addition(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y
    return render(request, 'result.html', {'result': add, 'subtraction': sub, 'res': mul, 'division': div})
