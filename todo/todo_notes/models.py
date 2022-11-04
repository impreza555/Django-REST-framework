from django.db import models

from users.models import Users


class Project(models.Model):
	name = models.CharField(max_length=32, unique=True, verbose_name='Название')
	link = models.URLField(blank=True, verbose_name='Ссылка')
	users = models.ManyToManyField(Users, verbose_name='Пользователи')
	
	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name_plural = 'Проекты'
		verbose_name = 'Проект'


class TodoNote(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
	text = models.TextField(verbose_name='Текст')
	creaton_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
	modifided_date = models.DateField(auto_now=True, verbose_name='Дата изменения')
	user = models.ForeignKey(Users, on_delete=models.PROTECT, verbose_name='Пользователь')
	is_active = models.BooleanField(default=True, verbose_name='Активно')
	
	class Meta:
		verbose_name_plural = 'Заметки'
		verbose_name = 'Заметка'
