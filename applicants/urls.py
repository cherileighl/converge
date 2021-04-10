from django.urls import path
from .views import allApplicantsView, loginStudentView, studentProfileView, createStudentView

urlpatterns = [
    path('all/', allApplicantsView, name="allApplicants"),
    path('login/', loginStudentView, name="loginStudent"),
    path('profile/', studentProfileView, name="studentProfile"),
    path('create/', createStudentView, name="createStudent"),
    # applicant log in
    # path('pathname', viewName, name="myViewName")
    # create profile
    # edit profile
    # delete profile
    # view jobs 
]