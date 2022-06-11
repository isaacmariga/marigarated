from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg



# Create your models here.

class Projects(models.Model):
	title = models.CharField(max_length =30)
	image = models.ImageField(upload_to = 'project_images')
	description = models.TextField(max_length =300)
	link = models.URLField(max_length=200)
	user = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
			return self.title

	def save_project(self):
			self.save()

	@classmethod
	def get_all(cls):
			table = Projects.objects.all()
			return table

	@classmethod
	def get_by_title(cls, title):
			table = Projects.objects.get(title=title)
			return table

	@classmethod
	def get_by_id(cls, id):
			table = Projects.objects.get(id=id)
			return table

	@classmethod
	def filter_by_title(cls, search):
			table = Projects.objects.filter(title__icontains=search)
			return table


class Profile(models.Model):
	picture = models.ImageField(upload_to = 'profile_images')
	bio = models.TextField(max_length =300)
	user = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return str(self.id)


	def save_table(self):
			self.save()

	@classmethod
	def get_by_user(cls, user):
		profile = cls.objects.filter(user__username=user).first()
		return profile

RATING = (
(1,1),
(2,2),
(3,3),
(4,4),
(5,5)
)
class Review(models.Model):
	comment =models.TextField(max_length=300)
	design_rating = models.IntegerField(choices=RATING,null = True,)
	content_rating = models.IntegerField(choices=RATING,null = True,)
	user_experience_rating = models.IntegerField(choices=RATING,null = True,)
	user = models.ForeignKey(User,on_delete=models.CASCADE, null = True, blank=True)
	project = models.ForeignKey(Projects,on_delete=models.CASCADE, null = True, blank=True)


	def __str__(self):
		return self.comment

	@classmethod
	def get_by_project(cls, project):
			table = Projects.objects.get(project=project)
			return table

	@classmethod
	def design_avg(cls):
			table = list(Review.objects.all().aggregate(Avg('design_rating')).values())
			table = round(float("".join(map(str,table))),2)
			return table

	@classmethod
	def content_avg(cls):
			table = list(Review.objects.all().aggregate(Avg('content_rating')).values())
			table = round(float("".join(map(str,table))),2)
			return table

	@classmethod
	def user_avg(cls):
			table = list(Review.objects.all().aggregate(Avg('user_experience_rating')).values())
			table = round(float("".join(map(str,table))),2)
			return table

	