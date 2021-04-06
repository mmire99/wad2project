from django.db import models
from django.contrib.auth.models import User as U
class Profile(models.Model):
	user = models.OneToOneField(U,on_delete=models.CASCADE)
	profile_pic = models.ImageField(default='default.jpg')

	def __str__(self):
		return '{} Profile'.format(self.user.username)