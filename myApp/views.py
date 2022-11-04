from django.shortcuts import render, redirect, get_list_or_404
# jsonResponse es para que nosotros podamos devolver un formato que el navegadro puede entender facilmente
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject


def index(request):
    title = 'Django courses !!'
    return render(request, 'index.html', {
        'title': title
    })


def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)


def about(request):
    username = 'Anibal'
    return render(request, 'about.html', {
        'username': username
    })


def projects(request):
    # traigo todos los datos que tengo en la base de datos
    projects = Project.objects.all()
    # projects= list(Project.objects.values  ()) #esto lo que hace es traerme un array de todos los objetos proyectos desde la base de datos
    return render(request, 'projects.html', {
        'projects': projects
    })


def tasks(request):
    task = Task.objects.all()
    # task=Task.objects.get(id=id) # el primer parametro es el atributo de la entidad y el segudo es el valor id que le paso por parametro
    return render(request, 'tasks.html', {
        'tasks': task
    })


def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': CreateNewTask()})
    else:
        Task.objects.create(
            title=request.POST['title'], descripcion=request.POST['description'], project_id=1)
        return redirect('tasks')


def create_projects(request):
    if request.method == 'GET':
        return render(request, 'create_projects.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')


def projects_detail(request, id):
    project=get_list_or_404(Project, id=id)
    tasks=Task.objects.filter(project_id=id)
    return render(request, 'detail.html', {
        'project':project,
        'tasks':tasks
    })