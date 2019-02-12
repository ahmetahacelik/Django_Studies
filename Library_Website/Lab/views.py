# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import models
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.http import HttpResponseRedirect
from Lab.models import BlockPost

# Create your views here.
def DisplayAllProjects(request):
   Projects=models.Project.objects.all()
   context={"Projects":Projects}

   return render(request, "Projects.html", context)

def DisplaySingleProject(requst,pid):
    Proj=pid.replace("Project/","")
    Proj= models.Project.objects.get(Name=Proj)

    #Proj = models.Project.objects.get(pk = pid)
    return render(requst,"SingleProject.html",{"ProjectName":Proj})

def DisplayAllPeople(request):

    Workers2=models.Worker.objects.all()
    context = {"Workers2": Workers2}

    return render(request,"People.html",context)

def DisplayBlogs(requst):

    all_blogs=BlockPost.objects.all()
    print(all_blogs)

    return render(requst, "Blogs.html",{'blogs':all_blogs})

def DisplayPost(requst):
    if requst.method=="POST":
        form = ContactForm(requst.POST)
        form.save()
        return HttpResponseRedirect('/Lab/Blogs/')

    else:
        form=ContactForm()
        return render(requst, "Submit.html", {'form':form})



def DisplaySinglePerson(requst,pid):
    PersonName=pid.replace("People/","").split("_")
    PersonName=models.Worker.objects.get(FirstName=PersonName[0])
    return render(requst,"SingleWorker.html",{"PersonName":PersonName})

def Home(request):
    return render(request,"home.html")
