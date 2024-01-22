from django.db import models

# Create your models here.


class products(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2 , default=99.9) 


    