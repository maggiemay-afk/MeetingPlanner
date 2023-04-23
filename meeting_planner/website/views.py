from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting


# Create your views here.

def welcome(request):
    return render(request, "Website/welcome.html", {"meetings": Meeting.objects.all()})


def date(request):
    return HttpResponse("This page was served at: " + str(datetime.now()))


def about(request):
    return HttpResponse("This is a website created by Maggie Herms for APC440")
