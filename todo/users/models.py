from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
	username = models.CharField(verbose_name="username", max_length=64, unique=True)
	first_name = models.CharField(verbose_name="first name", max_length=64)
	last_name = models.CharField(verbose_name="last_name", max_length=64)
	email = models.EmailField(verbose_name="email address", unique=True)
