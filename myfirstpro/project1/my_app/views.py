from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import My_app
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def Student_data(request):
    data=My_app.objects.all().values()
    context ={
        'data':data
    }
    return render(request,'index.html',context)

def add(request):
    x=request.POST['rno']
    y=request.POST['name']
    data=My_app(rollnumber=x,studentname=y)
    data.save()

    return HttpResponseRedirect(reverse(Student_data))

def delete(request,id):
    data=My_app.objects.get(id=id)
    data.delete()

    return HttpResponseRedirect(reverse(Student_data))

def update(request,id):
    if request.method != 'POST':
        data=My_app.objects.get(id=id)
        return render(request, 'update.html', {'data':data})
    else:
        m=request.POST['rno']
        n=request.POST['name']
        data=My_app.objects.get(id=id)
        data.rollnumber=m
        data.studentname=n
        data.save()
        return HttpResponseRedirect('/')
