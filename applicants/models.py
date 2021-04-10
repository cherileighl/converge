from django.db import models
import phonenumbers

# Create your models here.
class Review(models.Model):
    review = models.CharField(max_length=1000)
    company = models.ForeignKey('Company', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return (self.review)

class Job(models.Model):
    company = models.ForeignKey('Company', null=True, blank=True, on_delete=models.SET_NULL)
    industry = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100)
    location = models.ForeignKey('Location', null=True, blank=True, on_delete=models.SET_NULL)    
    start_date = models.DateField()
    job_type = models.ForeignKey('Type', null=True, blank=True, on_delete=models.SET_NULL)
    hourly_pay = models.FloatField()
    qualifications = models.CharField(max_length=300)
    description = models.CharField(max_length=500)

    def __str__(self):
        return (self.job_title)

# Type of job (i.e., full-time, part-time, internship)
class Type(models.Model):
    type_desc = models.CharField(max_length=20)

    def __str__(self):
        return (self.type_desc)

class Location(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return (self.city + ', ' + self.state)

class Education(models.Model):
    school = models.CharField(max_length=100)
    gpa = models.FloatField()
    major = models.CharField(max_length=50)
    graduation_date = models.DateField()

    def __str__(self):
        return (self.school)

class Experience(models.Model):
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    location = models.ForeignKey('Location', null=True, blank=True, on_delete=models.SET_NULL)
    start_date = models.DateField()
    end_date = models.DateField()
    # TO-DO ~ if current position, handle with property?
    description = models.CharField(max_length=300)

    def __str__(self):
        return (self.position)

class Skill(models.Model):
    skill_name = models.CharField(max_length=30)

    def __str__(self):
        return (self.skill_name)

class Company(models.Model):
    company_name = models.CharField(max_length=50)
    company_desc = models.CharField(max_length=500)
    company_email = models.CharField(max_length=100)
    company_password = models.CharField(max_length=30)

    def __str__(self):
        return (self.company_name)

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    verified = models.BooleanField()
    education = models.ManyToManyField(Education, blank=True)
    experience = models.ManyToManyField(Experience, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    reviews = models.ManyToManyField(Review, blank=True)

    def __str__(self):
        return (self.first_name + ' ' + self.last_name)






