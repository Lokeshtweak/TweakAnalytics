from django.db.models.functions import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def siva(request):
    return HttpResponse("<p> hello siva krishna welcome to django </p>")
def today_is(request):
    now = datetime.datetime.now()
    html = "<p>Current date and time is :{0}</p>".format(now)
    return HttpResponse(now)