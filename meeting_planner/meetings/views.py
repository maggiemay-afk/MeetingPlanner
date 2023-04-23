from django.shortcuts import render, get_object_or_404
from django.forms import modelform_factory
from .models import Meeting


# Create your views here.
def detail(request, id):
    meeting = Meeting.objects.get(pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


MeetingForm = modelform_factory(Meeting, exclude=[])


def new(request):
    form = MeetingForm()
    return render(request, 'meetings/new.html', {"form": form})
