from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .search import *
from .models import Project
from .forms import SearchForm, DetailsForm

def index(request):
    form = SearchForm()
    return render(request, 'archive/index.html', {'form': form})
    
def results(request):
    form = SearchForm(request.GET or None)
    if form.is_valid():
        query_string = ''
        found_projects = None
        #Get query string
        query_string = request.GET['q']
        #Get a list of projects from the query string
        entry_query = get_query(query_string, ['year', 'groupName', 'students__name', 'client__organization', 'client__person',])
        found_projects = Project.objects.filter(entry_query).distinct()            
        return render(request, 'archive/results.html', { 'query_string': query_string, 'found_projects': found_projects})       

    return render(request, 'archive/index.html', {'form': form})

def details(request):
    if request.method == 'POST':
        #Get list of the selected projects        
        project_list = request.POST.getlist('project')
        selected_projects = Project.objects.filter(pk__in=project_list).distinct()
        #TODO Check at least one project has been selected
        if selected_projects.count() == 0:
            #get query string
            query_string = request.POST['q']    
            return redirect(reverse('results')+'?q='+query_string)
            
        form = DetailsForm()
        return render(request, 'archive/details.html', {'selected_projects': selected_projects, 'form': form})
    else:
        form = SearchForm()
        return render(request, 'archive/index.html', {'form': form})

def confirmation(request):
    if request.method == 'POST':
        #Get list of selected projects(this should always be at least one)
        #TODO Check again?
        selected_projects = request.POST.getlist('project')
        
        form = DetailsForm(request.POST)
        if form.is_valid():
            #TODO Get email address/user name etc
            #TODO Format email and send off
            return render(request, 'archive/confirmation.html', {'selected_projects': selected_projects, 'name': name, 'email': email})
        else:
            #name/email isn't valid, send back to previous page to get details
            return render(request, 'archive/details.html', {'selected_projects': selected_projects, 'form': form})
    else:
        form = SearchForm()
        return render(request, 'archive/index.html', {'form': form})    
