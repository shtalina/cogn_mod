from django.shortcuts import render
from django.http import HttpResponse
from .models import Students


def Stud(request):
    data = Students.objects.all()
    return render(request, 'cogn/stud.html', {'data': data})