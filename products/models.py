from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Distributer(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=250)

    class Meta:
        db_table = 'distributer'


class Product(models.Model):
    name = models.CharField(max_length=100, default="Test Product")
    price = models.FloatField()
    quantity = models.IntegerField(null=True, blank=True)
    is_availible = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="products")
    distributers = models.ManyToManyField(Distributer)

    def __str__(self):
        return self.name + " - " + str(self.id)

    class Meta:
        # abstract = True
        db_table = 'product'
        ordering = ['-price', 'created']
