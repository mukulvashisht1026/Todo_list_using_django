from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import *
from .models import List
def index (request):
	form = Todo_list()
	all_objects=List.objects.all()
	return render(request,'list/home.html',{'form':form,'all_objects':all_objects})

def add(request):
	if request.method=='POST':
		obj=List(text=request.POST['TASKS'])
		obj.save()
		return redirect(index)
def delete(request):
	obj = List.objects.all()
	for i in obj:
		if(i.check):
			i.delete()

	return redirect('index')

def complete(request,todo_id):
	todo = List.objects.get(pk=todo_id)
	todo.check = True
	todo.save()
	return redirect('index')