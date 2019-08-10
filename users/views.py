from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def sukumar_function(request):
    return render(request, 'sukumar.html')