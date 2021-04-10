from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def allApplicantsView(request):
    data = Student.objects.all()

    context = {
        "students": data
    }
    
    return render(request, 'applicants/allapplicants.html', context)

def loginStudentView(request):
    return render(request, 'applicants/login.html')

def studentProfileView(request):
    return render(request, 'applicants/profile.html')

def createStudentView(request):
    return render(request, 'applicants/create.html')