from rest_framework.serializers import ModelSerializer, StringRelatedField
from todo_notes.models import Project, TodoNote
from users.serializers import UsersModelSerializer


class ProjectSerializer(ModelSerializer):
	# users = StringRelatedField(many=True)
	users = StringRelatedField(many=True)
	
	class Meta:
		model = Project
		fields = '__all__'


class TodoNoteSerializer(ModelSerializer):
	user = UsersModelSerializer()
	
	class Meta:
		model = TodoNote
		fields = '__all__'
