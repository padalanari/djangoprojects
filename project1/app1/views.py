from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloDjango(request):
    message="Hello, Welcome Django world"
    return HttpResponse(message)
