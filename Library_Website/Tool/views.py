from django.shortcuts import render
from .forms import ToolForm
from django.http import HttpResponseRedirect
from . import Histogram

# Create your views here.

def Home(request):
    if request.method=="POST":
        form = ToolForm(request.POST)
        texting=form["text"].value()
        result=Histogram.hist(texting)
        return render(request, "table_part.html", {'result': result})
    else:
        form=ToolForm()
        return render(request, "Tool2.html", {'form':form})