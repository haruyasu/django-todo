from django.db import models


class Todo(models.Model):
	title = models.CharField("タイトル", max_length=200)
	deadline = models.DateField("期限")

	def __str__(self):
		return self.title
