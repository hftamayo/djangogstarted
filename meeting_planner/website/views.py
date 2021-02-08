from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from datetime import datetime

from meetings.models import Meeting

def welcome(request):
    return render(request, "website/welcome.html",
                  {"meetings": Meeting.objects.all()})

def date(request):
    return HttpResponse("This page was served at: " + str(datetime.now()))

def about(request):
    return HttpResponse("This code is based on Pluralsight's Django "
                        "Getting Started by Reindert-Jan Ekker")