from django.shortcuts import render, get_object_or_404
from .models import Project, Message
from .forms import ContactForm

def home(request):
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    return render(request, 'home.html', {'featured_projects': featured_projects})


def projects(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'projects.html', {'projects': projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project_detail.html', {'project': project})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
