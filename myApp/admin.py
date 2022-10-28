from django.contrib import admin
from .models import Post, Project, Task


admin.site.register(Project)
admin.site.register(Task)
