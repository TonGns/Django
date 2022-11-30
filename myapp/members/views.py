from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members
from django.urls import reverse



# Create your views here.
def index(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mymembers
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    emp_id = request.POST['emp_id']
    image = request.POST['image']
    fname = request.POST['fname']
    lname = request.POST['lname']
    gender = request.POST['gender']
    age = request.POST['age']
    member = Members(emp_id = emp_id, image = image, fname = fname, lname = lname, gender = gender, age = age)
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, emp_id):
    member = Members.objects.get(emp_id = emp_id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, emp_id):
    mymember = Members.objects.get(emp_id = emp_id)
    template = loader.get_template('update.html')
    context = {
        'mymember': mymember
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, emp_id):
    fname = request.POST['fname']
    lname = request.POST['lname']
    gender = request.POST['gender']
    age = request.POST['age']

    member = Members.objects.get(emp_id = emp_id)
    member.fname = fname
    member.lname = lname 
    member.gender = gender
    member.age = age
    member.save()
    return HttpResponseRedirect(reverse('index'))
