from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)
	email=models.EmailField(max_length=254,unique = True,error_messages ={
					"unique":"The email you entered is already used. Please Enter another email"
					})
	password=models.CharField(max_length=20)
	username=models.CharField(max_length=30,unique = True,error_messages ={
					"unique":"The username you entered is not unique."
					})
	# a_qualification=models.CharField(max_length=50) It can be accessed using POST object no need to create field for it
	# t=[('Student','Student'),('Student','Author')]
	role=models.CharField(default='Student',max_length=20)

	def __str__(self):
		return self.username

	def uid(self):
		return self.id

class Student(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	s_name=models.CharField(max_length=30)
	email=models.EmailField(max_length=254)
	def __str__(self):
		return self.s_name
	

class Author(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	a_name=models.CharField(max_length=30)
	a_qualification=models.CharField(max_length=50)
	email=models.EmailField(max_length=254)
	proof=models.ImageField(upload_to="author_proof",default='1.jpg')
	status=models.CharField(max_length=30,default="Pending")
	
	
	
	def __str__(self):
		return self.a_name

class Video(models.Model):
	title=models.CharField(max_length=36,help_text = "Title should not exceed 36 characters")
	banner=models.ImageField(upload_to="images/",default='1.jpg')
	video=models.FileField(upload_to="video/")
	author=models.ForeignKey(Author,on_delete=models.CASCADE)
	enrolled_student = models.ManyToManyField(Student,blank=True, null=True)
	status=models.CharField(max_length=30,default="Pending")

	def __str__(self):
		return self.title