from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Client(models.Model):
    organization = models.CharField(max_length = 128, default = 'None')
    person = models.CharField(max_length = 128, blank = True)
    contact = models.CharField(max_length = 128, blank = True)

    def __unicode__(self):
        return self.organization + ', ' + self.person

class Student(models.Model):
    name = models.CharField(max_length = 128, unique = True, null = False)

    def __unicode__(self):
        return self.name

class Project(models.Model):
    year = models.IntegerField()
    groupName = models.CharField(max_length = 128, unique = True)
    client = models.ForeignKey(Client)
    students = models.ManyToManyField(Student)

    def __unicode__(self):
        return self.groupName


