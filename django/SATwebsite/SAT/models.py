from django.db import models

class Team(models.Model):
	identifier =models.CharField(max_length=250)
	teamNr =models.CharField(max_length=100)
	teamName=models.CharField(max_length=250)
	teamID =models.CharField(max_length=250)
	name=models.CharField(max_length=250,default='')
	year=models.CharField(max_length=4)
	rond=models.CharField(max_length=100,default='0')
	size=models.CharField(max_length=5,default='')


	def __str__(self):
		return self.name

class User(models.Model):
	userID =models.CharField(max_length=25)
	password=models.CharField(max_length=250)
	title=models.CharField(max_length=25)
	initials=models.CharField(max_length=25)
	name=models.CharField(max_length=250)
	surname=models.CharField(max_length=250)
	cellphone=models.CharField(max_length=25)
	emailaddress=models.CharField(max_length=250)
	status=models.CharField(max_length=5)

	def __str__(self):
		return self.name


class MBTI(models.Model):
	userID =models.CharField(max_length=250)
	Type=models.CharField(max_length=250)
	
	def __str__(self):
		return self.userID

class participatoryentity(models.Model):
	"""docstring for Participatory"""
	userID =models.CharField(max_length=250)
	teamID=models.CharField(max_length=250)
	Type =models.CharField(max_length=250)
	value=models.CharField(max_length=250)

	def __str__(self):
		return self.userID

class bellbin(models.Model):
	userID =models.CharField(max_length=250)
	SH=models.CharField(max_length=10)
	IM=models.CharField(max_length=10)
	CF=models.CharField(max_length=10)
	CO=models.CharField(max_length=10)
	RI=models.CharField(max_length=10)
	PL=models.CharField(max_length=10)
	ME=models.CharField(max_length=10)

	def __str__(self):
		return self.userID

class teamattributes(models.Model):
	teamID =models.CharField(max_length=250)
	diversity =models.CharField(max_length=10)

	def __str__(self):
		return self.teamID

class teamRank(models.Model):
	teamID =models.CharField(max_length=250)
	rankmatrix =models.CharField(max_length=250)

	def __str__(self):
		return self.teamID

class teamQuality(models.Model):
	teamID =models.CharField(max_length=250)
	qualitymatrix =models.CharField(max_length=250)

	def __str__(self):
		return self.teamID

class teamHours(models.Model):
	teamID =models.CharField(max_length=250)
	hoursmatrix =models.CharField(max_length=250)

	def __str__(self):
		return self.teamID

class teamMBTI(models.Model):
	teamID =models.CharField(max_length=250)
	mbtimatrix =models.CharField(max_length=250)

	def __str__(self):
		return self.teamID

class teambellbin(models.Model):
	teamID =models.CharField(max_length=250)
	bellbinmatrix =models.CharField(max_length=250)

	def __str__(self):
		return self.teamID