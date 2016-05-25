import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'archive_project.settings')

import django
django.setup()

from archive.models import Client, Project, Student
from django.db import models

def populate(textfile):
    print "Opening up " + textfile + " for importation"

    #Load text file and iterate over contents
    with open(textfile,'r') as fh:
        for line in fh:
            #strip off new line character
            line=line.rstrip()
            #Check to see if this as a project line
            if line.find('\t') != 0:
                details = line.split(';')
                #Create Client
		client = add_client(details[2], details[3], details[4])
                #Create Project
                project = add_project(details[0], details[1], client)
            else:
                #Create student
                student = add_student(line[1:], project)

    #Loop over contents of file
    #If it doesnt start with a tab:
    #    Explode string(regex?)
    #    Create client 'client'
    #    Create project 'project' using 'client' and exploded data
    #elif
    #    Create student with 'project' reference
    

def add_client(organization, person, contact):
    c = Client.objects.get_or_create(organization = organization, person = person)[0]
    print contact
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
    print "-------------------------------------"

    print "Deleting old data"
    Client.objects.all().delete()
    Project.objects.all().delete()
    Student.objects.all().delete()

    print "Loading new data from text file"
    populate('testdata.txt')
