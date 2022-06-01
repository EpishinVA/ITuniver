from django.db import models


class Task(models.Model):
	title = models.CharField('Фио',max_length=50)
	task = models.TextField('Содержание')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Обращение'
		verbose_name_plural = 'Обращение'