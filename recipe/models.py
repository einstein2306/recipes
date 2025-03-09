from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    ingredients = models.TextField()
    process = models.TextField(null=True,blank=True)

    def __str__(self):
        return f"{self.title}" 