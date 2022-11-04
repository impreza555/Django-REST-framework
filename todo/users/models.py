from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
	email = models.EmailField(unique=True)
	
	def __str__(self):
		return self.username
	
	class Meta:
		verbose_name_plural = 'Пользователи'
		verbose_name = 'Пользователь'
