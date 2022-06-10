from venv import create
from django.shortcuts import render, redirect
from .models import Project
from .form import ProjectForm

# Create your views here.
def home(request):
    return render(request, 'portfolio/home.html')


# def add_project(request):
    
#     add_project = ProjectForm()
#     if request.method == 'POST':
#         add_project = ProjectForm(request.POST)
#         if add_project.is_valid():
#             add_project.save()
#             return redirect('web-development')
    


def web_project(request):
    projects = Project.objects.all()

    add_project = ProjectForm()
    if request.method == 'POST':
        add_project = ProjectForm(request.POST)
        if add_project.is_valid():
            add_project.save()
            return redirect('web-development')

    context = {
        'projects': projects,
        'add_project': add_project,
    }

    return render(request, 'portfolio/web-applications-projects.html', context)
