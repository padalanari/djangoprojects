from django.shortcuts import render

# Create your views here.
def showIndex(request):
    render(request,"main.html")
