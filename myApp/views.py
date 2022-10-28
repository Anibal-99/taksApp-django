from django.shortcuts import render
from django.http import HttpResponse, JsonResponse # jsonResponse es para que nosotros podamos devolver un formato que el navegadro puede entender facilmente
from .models import Project, Task


def index(request):
    title= 'Django courses !!'
    return render(request, 'index.html', {
        'title':title
    })

def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" %username)

def about(request):
    username='Anibal'
    return render(request, 'about.html', {
        'username':username
    })

def projects (request):
    projects= Project.objects.all() #traigo todos los datos que tengo en la base de datos
    #projects= list(Project.objects.values  ()) #esto lo que hace es traerme un array de todos los objetos proyectos desde la base de datos
    return render(request, 'projects.html',{
        'projects':projects
    })

def tasks(request):
    task=Task.objects.all()
    #task=Task.objects.get(id=id) # el primer parametro es el atributo de la entidad y el segudo es el valor id que le paso por parametro
    return render(request,'tasks.html',{
        'tasks':task
    })