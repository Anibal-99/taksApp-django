from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Task(models.Model):
    title= models.CharField(max_length=200)
    descripcion=models.TextField()
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    done= models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' - ' + self.project.name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
