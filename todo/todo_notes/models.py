from django.db import models

from users.models import Users


class Project(models.Model):
	name = models.CharField(max_length=32)
	link = models.CharField(max_length=128, blank=True)
	users = models.ManyToManyField(Users)
	
	def __str__(self):
		return self.name


class TodoNote(models.Model):
	project = models.OneToOneField(Project, on_delete=models.CASCADE)
	text = models.TextField()
	creaton_date = models.DateField(auto_now_add=True)
	modifided_date = models.DateField(auto_now=True)
	user = models.ForeignKey(Users, models.PROTECT)
	is_active = models.BooleanField(default=True)
