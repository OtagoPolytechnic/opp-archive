from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .search import *
from .models import Project
from .forms import SearchForm, DetailsForm
from django.core.mail import send_mail
import os

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
        #Check at least one project has been selected
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
        project_list = request.POST.getlist('project')
        selected_projects = Project.objects.filter(pk__in=project_list).distinct()
        
        form = DetailsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name         = data['name']
            organisation = data['organisation']
            email        = data['email']
            #Format email and send off
            subject = "Opp-archive request from "+name
            #Add organisation name if avaliable
            if (organisation!=''):
                subject+=" at "+organisation
            
            #Created message
            message = "The following project(s) have been requested:\n"
            for project in selected_projects:
                request_line = "* " + str(project.year) + " - " + project.groupName +"\n"
                message += request_line
            
            #Send email
            #TODO Uncomment once SMTP server is set up
            #TODO Deal with failure?
            #send_mail(subject, message, email, ['dickaj1@student.op.ac.nz'], fail_silently=False)
            
            #Log to file
            my_dir = os.path.dirname(__file__)
            log_file_path = os.path.join(my_dir, 'requestLog.txt')
            
            with open(log_file_path, 'a') as file_object:
                file_object.write(subject+"\n")
                file_object.write(message+"\n")
                file_object.write(email+"\n")
                file_object.write("-------------------------------------\n")
            
            return render(request, 'archive/confirmation.html', {'selected_projects': selected_projects, 'name': name, 'email': email})
        else:
            #name/email isn't valid, send back to previous page to get details
            return render(request, 'archive/details.html', {'selected_projects': selected_projects, 'form': form})
    else:
        form = SearchForm()
        return render(request, 'archive/index.html', {'form': form})    
