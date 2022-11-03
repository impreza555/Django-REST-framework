from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, HyperlinkedRelatedField
from todo_notes.models import Project, TodoNote


class ProjectSerializer(ModelSerializer):
	# users = HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)
	
	class Meta:
		model = Project
		fields = '__all__'


class TodoNoteSerializer(ModelSerializer):
	# user = HyperlinkedIdentityField(view_name='user-detail')
	
	class Meta:
		model = TodoNote
		exclude = ('is_active',)
