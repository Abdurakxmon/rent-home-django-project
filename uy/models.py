from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User,blank=True,null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=50, null=True)
	phone= models.CharField(max_length=50,null=True)

	def __str__(self):
		return f'user - {self.user.username}'
		

class New_home(models.Model):
	user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
	region = models.CharField(max_length=150)
	district = models.CharField(max_length=150)
	cost = models.CharField(max_length=100)
	number_of_rooms = models.CharField(max_length=100)
	desc = models.TextField()
	date = models.DateTimeField(auto_now_add=True, null=True)
	img_1 = models.ImageField(upload_to="home_images/")
	img_2 = models.ImageField(upload_to="home_images/")
	img_3 = models.ImageField(upload_to="home_images/")


	class Meta:
		verbose_name = 'home'
		verbose_name_plural = 'homes'


	def __str__(self):
		return f"Home - {self.region}"

class Contact(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	number = models.CharField(max_length=50)
	message = models.TextField()

	def __str__(self):
		return f"message - {self.name}"