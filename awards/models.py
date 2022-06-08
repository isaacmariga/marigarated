from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Projects(models.Model):
	title = models.CharField(max_length =30)
	image = models.ImageField(upload_to = 'project_images')
	description = models.TextField(max_length =300)
	link = models.URLField(max_length=200)
	user = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
			return self.title

	def save_table(self):
			self.save()

	@classmethod
	def get_all(cls):
			table = Projects.objects.all()
			return table

	@classmethod
	def get_by_title(cls, title):
			table = Projects.objects.get(title=title)
			return table


class Profile(models.Model):
	picture = models.ImageField(upload_to = 'profile_images')
	bio = models.TextField(max_length =300)
	user = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return str(self.id)


	def save_table(self):
			self.save()
