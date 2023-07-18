from django.shortcuts import render # to render template
from django.http import HttpResponse #object created using rendered templates
from django.template import Template,Context
from diseaseprediction import *


# Create your views here.
def home(request):
    return render(request, "home.html")


def projects(request):
    return render(request, "projects.html")


def contact(request):
    if request.method == 'POST': #when user clicks a submit button
        symple1 = request.POST.get('symp1')
        symple2 = request.POST.get('symp2')
        symple3 = request.POST.get('symp3')
        symple4 = request.POST.get('symp4')
        symple5 = request.POST.get('symp5')
        symple6 = request.POST.get('symp6')
        symple7 = request.POST.get('symp7') #options
        r=predict(symple1, symple2, symple3, symple4, symple5, symple6, symple7)
        context={
           "symple1": symple1,
            "symple2": symple2,
            "symple3": symple3,
            "symple4": symple4,
            "symple5": symple5,
            "symple6": symple6,
           "symple7": symple7,
            "rs": r,
        }
        return render(request, "prediction_here.html", context)
    return render(request, "prediction_here.html")
