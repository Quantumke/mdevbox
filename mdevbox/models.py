from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django_mongoengine import Document, EmbeddedDocument, DynamicDocument
from django_mongoengine import fields
from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import permalink

# Create your models here.

class reg_user(models.Model):
    user = models.OneToOneField(User)
    role=models.CharField(max_length=100, unique=False)


    def __unicode__(self):
        return self.user.username

class developers_employment(models.Model):
    email=models.CharField(max_length=100, unique=True)
    speciality=models.CharField(max_length=100, unique=False)
    previous_employer=models.CharField(max_length=100, unique=False)
    role_previous_employment=models.CharField(max_length=100, unique=False)
    begin_previous_employment=models.DateField(blank=False)
    end_previous_employment=models.DateField(blank=False)
    def __unicode__(self):
        return self.d.email


class developers_education(models.Model):
    email=models.CharField(max_length=100, unique=True)
    highest_education=models.CharField(max_length=100, unique=False)
    institute_name=models.CharField(max_length=100, unique=False)
    course=models.CharField(max_length=100, unique=False)
    begin_education=models.DateField(blank=False)
    end_education=models.DateField(blank=False)
    def __unicode__(self):
    	return self.user.email

class developers_portfolio(models.Model):
    email=models.CharField(max_length=100, unique=False)
    portfoli_name=models.CharField(max_length=100, unique=False)
    portfoli_tech=models.CharField(max_length=100, unique=False)
    portfoli_link=models.CharField(max_length=100, unique=False)
    portfoli_desc=models.CharField(max_length=100, unique=False)
    def __unicode__(self):
        return self.user.email


class hire(models.Model):
    company=models.CharField(max_length=100, unique=False)
    job_title=models.CharField(max_length=100, unique=False)
    job_description=models.CharField(max_length=100, unique=False)
    date = models.DateField(default=datetime.now, blank=False)



class post_job(models.Model):
    job_title=models.CharField(max_length=100, unique=False)
    job_description=models.CharField(max_length=100, unique=False)
    company= models.CharField(max_length=100, unique=False)
    pay=models.CharField(max_length=100, unique=False)
    date = models.DateField(default=datetime.now, blank=False)


