from django.shortcuts import render
from django.http import HttpResponse
from .search import *
from .models import Project

def index(request):
    return render(request, 'archive/index.html')
    
def search(request):
    query_string = ''
    found_projects = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']

        entry_query = get_query(query_string, ['year', 'groupName', 'students__name', 'client__organization', 'client__person',])
        found_projects = Project.objects.filter(entry_query).distinct()

    return render(request, 'archive/search_results.html',
                         { 'query_string': query_string, 'found_projects': found_projects })
