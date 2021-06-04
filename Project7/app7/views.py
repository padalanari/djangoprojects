from django.shortcuts import render

# Create your views here.
def showIndex(request):
    student_info={"data":
    [
        { "idno": 101,"name": "Ravi","marks":[89,56,74,15,45,56]},
        {"idno": 102, "name": "Nari", "marks": [45, 56, 74, 15, 45, 56]},
        {"idno": 103, "name": "Jyothi", "marks": [89, 56, 74, 15, 45, 56]},
        {"idno": 104, "name": "Lucky", "marks": [89, 56, 74, 15, 45, 56]},
        {"idno": 105, "name": "Babu", "marks": [89, 56, 74, 15, 45, 56]},
    ]
    }
    #dict_data={"data": student_info
    return render(request,"index.html",student_info)
