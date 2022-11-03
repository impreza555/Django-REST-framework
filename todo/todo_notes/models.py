from django.db import models

from users.models import Users


class Project(models.Model):
	name = models.CharField(max_length=32, unique=True)
	link = models.URLField(blank=True)
	users = models.ManyToManyField(Users)
	
	def __str__(self):
		return self.name


class TodoNote(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	text = models.TextField()
	creaton_date = models.DateField(auto_now_add=True)
	modifided_date = models.DateField(auto_now=True)
	user = models.ForeignKey(Users, on_delete=models.PROTECT)
	is_active = models.BooleanField(default=True)
