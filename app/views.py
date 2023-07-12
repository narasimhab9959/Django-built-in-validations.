from django.shortcuts import render
from app.forms import *
# Create your views here.
from django.http import HttpResponse


def sf(request):
    SFO=student_form()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=student_form(request.POST)
        if SFD.is_valid():
            return HttpResponse(str(SFD.cleaned_data))
        else:
            return HttpResponse('in_valid')
    return render(request,'sf.html',d)