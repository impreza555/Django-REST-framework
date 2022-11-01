from django.contrib import admin

from todo_notes.models import Project, TodoNote

admin.site.register(Project)
admin.site.register(TodoNote)
