from django.db import models

# Create your models here.

class Product(models.Model):
	title= models.CharField(max_length=20, default= False)
	description = models.TextField(null=False, default=False)
	price = models.DecimalField(max_digits=99999, decimal_places=2)
