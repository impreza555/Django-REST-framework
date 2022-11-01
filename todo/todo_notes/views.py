from rest_framework.viewsets import ModelViewSet

from todo_notes.models import Project, TodoNote
from todo_notes.serializers import ProjectSerializer, TodoNoteSerializer


class ProjectModelViewSet(ModelViewSet):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer


class TodoNoteModelViewSet(ModelViewSet):
	queryset = TodoNote.objects.all()
	serializer_class = TodoNoteSerializer
