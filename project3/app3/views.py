from django.http import HttpResponse

# Create your views here.
def showIndex(request):
    message='''
    <html>
        <body bgcolor="skyblue">
        <h1 style="color:white">
            <font size="8">
                Welcome to project3 using HTML
            </font>
         </h1>
        </body>
    </html>
    '''

    return HttpResponse(message)

