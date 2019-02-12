# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Project(models.Model):
    Name = models.CharField(max_length=250)
    Budget = models.IntegerField()
    Workers = models.ManyToManyField('Worker',blank=True)
    def __str__(self):
        return str(self.Name) + " - $" + str(self.Budget)

class Worker(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Age = models.IntegerField()
    CurrentProject = models.ForeignKey(Project,blank=True,on_delete=True)
    def __str__(self):
        return str(self.FirstName) + " " + str(self.LastName) + ", " + str(self.Age) + " years old"


class BlockPost(models.Model):
    Title=models.CharField(max_length=100)
    Body=models.TextField(max_length=10000000)