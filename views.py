from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def registerPage(request):
    return render(request,'user/register_page.html')


def loginPage(request):
    return render(request,'user/login_page.html')

def logIn(request):
    return HttpResponse('login successful/fail')

def logOut(request):
    return HttpResponse('logout user')