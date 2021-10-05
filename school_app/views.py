from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from . forms import *

# Create your views here.


def register_view(request):

    if request.method=='POST':
        e_id=request.POST.get('e_id')
        name = request.POST.get('name')
        age = request.POST.get('age')
        post = request.POST.get('post')
        salary = request.POST.get('salary')
        date=request.POST.get('date')
        obj=Register(e_id=e_id,name=name,age=age,post=post,salary=salary,date=date)
        obj.save()

    obj1=Register.objects.all()
    return render(request,'register_view.html',{'obj1':obj1})

def delete(request,reg_id):
    register=Register.objects.get(id=reg_id)
    if request.method=='POST':
        register.delete()
        return redirect('/')
    return render(request,'delete.html',{'register':register})

def update(request,id):
    register=Register.objects.get(id=id)
    form=Schoolforms(request.POST or None,instance=register)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'register':register,'form':form})

