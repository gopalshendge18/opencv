from django.shortcuts import render
from django.http import HttpResponse


def ind(request):
    context = {
        "logname" :"Gopal Shendge"
    }
    return render(request,'index.html', context)

# Create your views here.
