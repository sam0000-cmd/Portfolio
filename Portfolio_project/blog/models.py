from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=20)
	Date = models.DateField()
	body = models.TextField()
	image = models.ImageField(upload_to='images/')