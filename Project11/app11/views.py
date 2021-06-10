from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html")
def loginCheck(request):
    username=request.POST.get("t1") # username and password are local variables
    password=request.POST.get("t2")
    if username=="nari" and password="jyothi":
        return render(request, "welcome.html")
    else:
        return render(request,"error.html")