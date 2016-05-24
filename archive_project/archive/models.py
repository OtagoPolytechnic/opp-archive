from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Client(models.Model):
    organization = models.CharField(max_length = 128, default = 'None')
    person = models.CharField(max_length = 128, blank = True)
    contact = models.CharField(max_length = 128, blank = True)

    def __unicode__(self):
        return self.organization + ', ' + self.person

class Project(models.Model):
    year = models.IntegerField()
    groupName = models.CharField(max_length = 128, unique = True)
    client = models.ForeignKey(Client)

    def __unicode__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length = 128, unique = True, null = False)
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.name
