from django.shortcuts import render
from django.http import HttpResponse
from applicants.models import Company

# Create your views here.
def empCreateView(request):
    # check if form method is get or post
    if request.method == 'POST':
        new_company = Company()

        new_company.company_name = request.POST.get('company_name')
        new_company.company_desc = request.POST.get('company_desc')

    # Get list of all companies
    data = Company.objects.all()

    context = {
        "companies" : data
    }
    
    return render(request, 'employers/create.html', context)
    # sOutput = '<h1>Hello World</h1>'
    # return HttpResponse(sOutput)

def empProfileView(request):
    # find matching company profile
    sEmail = request.POST.get('company_email')
    sPassword = request.POST.get('company_password')
    data = Company.objects.filter(company_email=sEmail, company_password=sPassword)
    print('Email: ' + str(sEmail))
    print('Password: ' + str(sPassword))
    print('Data: ' + str(data))
    print(data.count())
    
    if data.count() > 0:
        context = {
            "company": data
        }
        return render(request, 'employers/profile.html', context)
    else:
        return HttpResponse("Username and/or password are incorrect.")
    # return render(request, 'employers/profile.html')
    

def empLoginView(request):
    return render(request, 'employers/login.html')

def empSaveView(request):
    if request.method == 'POST':
        new_company = Company()

        new_company.company_name = request.POST.get('company_name')
        new_company.company_email = request.POST.get('company_email')
        new_company.company_password = request.POST.get('company_password')
        new_company.company_desc = request.POST.get('company_desc')

        new_company.save()

        data = Company.objects.filter(company_email=new_company.company_email, company_password=new_company.company_password)

        if data.count() > 0:
            context = {
                "company": data
            }
            return render(request, 'employers/profile.html', context)
        else:
            return HttpResponse("Username and/or password are incorrect.")


def empReadView(request):
    return render(request, 'employers/profile.html')




    