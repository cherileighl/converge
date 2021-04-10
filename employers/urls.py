from django.urls import path
from .views import empCreateView, empProfileView, empLoginView, empSaveView, empReadView

urlpatterns = [
    path('login/', empLoginView, name='loginCompany'),
    path('create/', empCreateView, name='createCompany'),
    path('profile/', empProfileView, name='companyProfile'),
    path('save/', empSaveView, name="saveCompany"),
    path('view/', empReadView, name="viewProfile")
]