from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100, default="Test Product")
    price = models.FloatField()
    quantity = models.IntegerField(null=True, blank=True)
    is_availible = models.BooleanField(default=True)


# create table product (id int primary key, name varchar(100), price decimal, )
