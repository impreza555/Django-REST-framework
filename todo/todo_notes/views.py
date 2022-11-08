from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from todo_notes.filters import ProjectFilter
from todo_notes.models import Project, TodoNote
from todo_notes.serializers import ProjectSerializer, TodoNoteSerializer


class ProjectLimitOffsetPagination(LimitOffsetPagination):
	default_limit = 10


class TodoNoteLimitOffsetPagination(LimitOffsetPagination):
	default_limit = 20


class ProjectModelViewSet(ModelViewSet):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer
	pagination_class = ProjectLimitOffsetPagination
	filterset_class = ProjectFilter


class TodoNoteModelViewSet(ModelViewSet):
	queryset = TodoNote.objects.all()
	serializer_class = TodoNoteSerializer
	filterset_fields = ['project']
	pagination_class = TodoNoteLimitOffsetPagination
	
	def destroy(self, request, *args, **kwargs):
		partial = kwargs.pop('partial', True)
		instance = self.get_object()
		serializer = self.get_serializer(instance, data=request.data, partial=partial)
		serializer.is_valid(raise_exception=True)
		serializer.instance.is_active = False
		serializer.save()
		return Response(status=status.HTTP_206_PARTIAL_CONTENT)
