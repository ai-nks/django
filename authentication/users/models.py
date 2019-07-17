from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
	post = models.CharField(max_length=400,blank = True)
	usern = models.ForeignKey(User, on_delete=models.CASCADE ,default="")

	def __str__(self):
		return f"{self.usern} {self.post}"