
from django.http import HttpResponse

# Create your views here.
def showIndex(http_request):
    message="Welcome to Django"
    return HttpResponse(message)