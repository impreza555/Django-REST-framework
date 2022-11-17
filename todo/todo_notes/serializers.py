from rest_framework.serializers import ModelSerializer
from todo_notes.models import Project, TodoNote


class ProjectModelSerializer(ModelSerializer):
	class Meta:
		model = Project
		fields = '__all__'


class TodoNoteModelSerializer(ModelSerializer):
	class Meta:
		model = TodoNote
		fields = '__all__'
