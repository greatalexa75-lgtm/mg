from django.shortcuts import render
from django.http import HttpResponse
from . models import Employee
def home(request):
    return HttpResponse("hello")
def task(request):
    return render(request,'home.html')
def Show_employee(request):
    Emp=Employee.objects.all()
    return render(request,'show.html',{'Employee':Emp})