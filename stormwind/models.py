from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce.models import HTMLField

class Thread(models.Model):
	member = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length=155)
	content = HTMLField(blank=True,null=True)
	date_created = models.DateTimeField(default=timezone.now)
	category = models.CharField(max_length=155)
	likes = models.ManyToManyField(User,related_name='likes')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('detail-view',kwargs={'pk':self.pk})

	def total_likes(self):
		return self.likes.count()

class Category(models.Model):
	name = models.CharField(max_length=155)
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('home')