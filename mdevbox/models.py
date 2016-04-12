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

class developers(models.Model):
    user=models.OneToOneField(User)
    speciality=models.CharField(max_length=100, unique=False)
    email=models.CharField(max_length=100, unique=False)
    yoe=models.CharField(max_length=100, unique=False)

