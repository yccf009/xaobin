from django.db import models

# Create your models here.
class users(models.Model):
    blog_username = models.CharField(max_length=20)
    blog_link = models.CharField(max_length=50)


