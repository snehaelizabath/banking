from django.http import HttpResponse
from django.shortcuts import render, redirect


from homeapp.forms import MovieForm
from homeapp.models import Movie


# from . models import bank



# Create your views here.
def home(request):

    return render(request,'home.html')
def addition(request):
    name="kerala"
    return render(request,'branches.html',{'obj':name})
def logout(request):

    return render(request,'logout.html')

def login(request):

    return render(request,'login.html')

def registration(request):

    return render(request,'registration.html')
def branches(request):
    return render(request,'branches.html')


def bank(request):
        return render(request, 'bank.html')

    #
    # return render(request,'features.html',dict_bank)def features(request):
    # dict_bank= {
    #     'bank': features.objects.all()
    # }
