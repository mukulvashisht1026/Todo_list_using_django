from django.db import models

# Create your models here.
class List(models.Model):
	text=models.CharField(max_length=50)
	check=models.BooleanField(default=False)
	def __str__(self):
		return self.text