from django.db import models
import uuid
import os
import csv
# Create your models here.

def content_file_name1(instance, filename):
    filename = '%s-1.jpg' % (instance.id)
    foldername = '%s' % (instance.id)
    return os.path.join('facedatabase/'+foldername,filename)

def content_file_name2(instance, filename):
    filename = '%s-2.jpg' % (instance.id)
    foldername = '%s' % (instance.id)
    return os.path.join('facedatabase/'+foldername,filename)

def content_file_name3(instance, filename):
    filename = '%s-3.jpg' % (instance.id)
    foldername = '%s' % (instance.id)
    return os.path.join('facedatabase/'+foldername,filename)

def content_file_name4(instance, filename):
    filename = '%s-4.jpg' % (instance.id)
    foldername = '%s' % (instance.id)
    return os.path.join('facedatabase/'+foldername,filename)

def content_file_name5(instance, filename):
    filename = '%s-5.jpg' % (instance.id)
    foldername = '%s' % (instance.id)
    return os.path.join('facedatabase/'+foldername,filename)

class facedatabase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 264)
    image1 = models.ImageField(upload_to=content_file_name1)
    image2 = models.ImageField(upload_to=content_file_name2)
    image3 = models.ImageField(upload_to=content_file_name3)
    image4 = models.ImageField(upload_to=content_file_name4)
    image5 = models.ImageField(upload_to=content_file_name5)
    dob = models.DateField()
    dod = models.DateField()
    crimes = models.CharField(max_length = 264)
    Injail = models.CharField(max_length = 264)
    gang = models.CharField(max_length = 264)
    address = models.CharField(max_length = 264)
    def __str__(self):
        return self.name
