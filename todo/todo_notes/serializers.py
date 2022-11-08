from rest_framework.serializers import ModelSerializer
from todo_notes.models import Project, TodoNote


class ProjectSerializer(ModelSerializer):
	class Meta:
		model = Project
		fields = '__all__'


class TodoNoteSerializer(ModelSerializer):
	class Meta:
		model = TodoNote
		fields = '__all__'
