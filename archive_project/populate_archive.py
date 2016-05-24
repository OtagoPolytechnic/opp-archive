import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'archive_project.settings')

import django
django.setup()

from archive.models import Client, Project, Student

def populate():
    #TODOread from file and call functions to create the objects
    pass

def add_client(organization, person, contact):
    c = Client.objects.get_or_create(organization = organization, person = person)[0]
    c.contact = contact
    return c

def add_project(year, groupName, client):
    p = Project.objects.get_or_create(year = year, groupName = groupName, client = client)[0]
    return p

def add_student(name, project):
    s = Student.objects.get_or_create(name = name, project = project)[0]
    return s

# Start execution here!
if __name__ == '__main__':
    print "Starting archive population script..."
    populate()
