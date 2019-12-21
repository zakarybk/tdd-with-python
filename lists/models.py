from django.db import models

# Have to run - python manage.py makemigrations - to update stuff to make this work
class Item(models.Model):
	text = models.TextField(default='')