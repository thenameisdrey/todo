from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm
from django.utils import timezone

def index(request):
    todo_list = Todo.objects.filter(mydate__lte=timezone.now()).order_by('mydate')
    form = TodoForm()
    mydate = timezone.now()
    context = {'todo_list' : todo_list, 'form' : form, 'mydate' : mydate}
    return render (request, 'todo/index.html',  context)

@require_POST
def addTodo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        mydate = timezone.now()
        new_todo.save()
    return redirect('index')

def todoComplete(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    todo = Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')

def deleteAdd(request):
    Todo.objects.all().delete()

    return redirect('index')
