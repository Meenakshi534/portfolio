from django.shortcuts import render
from projects.models import Project

# Create your views here.
# creating a view for index page that shows list of posts
#this contains all the projects listed, we get it by using Project.objects.all().

def project_index(request):

    projects = Project.objects.all()
    context = {
        'projects': projects
    }

    return render(request, 'project_index.html', context)

# creating a view for detail page that shows details of a post using the primary key i.e id

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }

    return render(request, 'project_detail.html', context)


