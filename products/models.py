from django.db import models

# Create your models here.
class Product(models.Model):   
    title       =   models.CharField(max_length=200,null=False)
    description =   models.TextField()
    price       =   models.DecimalField(decimal_places=2, max_digits=1000)
    summary     =   models.TextField(blank=True, default="this is my product buy it")
    features    =   models.BooleanField(default=False)