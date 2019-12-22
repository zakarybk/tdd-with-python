from django.db import models


class List(models.Model):
	pass

# Have to run - python manage.py makemigrations - to update stuff to make this work
class Item(models.Model):
	text = models.TextField(default='')
	list = models.ForeignKey(List, default=None)
