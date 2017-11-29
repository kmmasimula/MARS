from django.db import models

class Team(models.Model):
	identifier =models.CharField(max_length=250)
	teamNr =models.CharField(max_length=100)
	teamName=models.CharField(max_length=250)


	def __str__(self):
		return self.identifier