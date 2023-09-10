from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from app.forms import *


def student_valid(request):
    SFEO = StudentForm()
    d={'SFEO':SFEO}
    if request.method == 'POST':
        SFDO = StudentForm(request.POST)
        if SFDO.is_valid():
            return HttpResponse(str(SFDO.cleaned_data))
        else:
            return HttpResponse('<h1 style="color:red;">Invalid data entered</h1>')
    return render(request,'student.html',d)