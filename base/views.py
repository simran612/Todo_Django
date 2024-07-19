from django.shortcuts import render, redirect
from .models import Todo

def home(request):
    todos_objs = Todo.objects.all()
    context = {'todos': todos_objs}
    return render(request,'index.html',context)
def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        print(name, description, status)
        Todo.objects.create(name=name, description=description, status=status)
        return redirect ('home')
    return render(request,'create.html')
def edit(request,pk):
    todo_objs=Todo.objects.get(id=pk)
    context = {'todos':todo_objs}
    if request.method=='POST':
        todo_objs.name = request.POST.get('name')
        todo_objs.description = request.POST.get('description')
        todo_objs.status = request.POST.get('status')
        todo_objs.save()
        return redirect('home')
    return render(request,'edit.html',context)
def delete(request, pk):
    todo_objs=Todo.objects.get(id=pk)
    todo_objs.delete()
    return redirect('home')

