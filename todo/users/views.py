from rest_framework.viewsets import ModelViewSet

from users.models import Users
from users.serializers import UsersModelSerializer


class UsersModelViewSet(ModelViewSet):
	queryset = Users.objects.all()
	serializer_class = UsersModelSerializer
