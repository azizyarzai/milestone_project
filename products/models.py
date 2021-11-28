from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100, default="Test Product")
    price = models.FloatField()
    quantity = models.IntegerField(null=True, blank=True)
    is_availible = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " - " + str(self.id)

    class Meta:
        # abstract = True
        db_table = 'product'
        ordering = ['-price', 'created']


class Test(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        managed = False
