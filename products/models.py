from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.utils.timesince import timesince

User = get_user_model()


# Create your models here.


class Distributer(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=250)

    class Meta:
        db_table = 'distributer'


CATEGORIES = (
    ("COM", "Computer"),
    ("CAM", "Camera"),
    ("PHN", "Phone"),
)


def check_for_phone(value):
    # if 'phone' in value:
    if '' in value:
        return True

    raise ValidationError("Name should contain phone.")


class Product(models.Model):
    name = models.CharField(max_length=20, validators=[
                            check_for_phone], error_messages={
                                'unique': 'the value is not unique',
                                'blank': 'please enter the name'
    }, help_text="Please enter a unique name!")
    slug = models.SlugField(unique=True)
    price = models.FloatField()
    quantity = models.IntegerField(null=True, blank=True)
    is_availible = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="products")
    distributers = models.ManyToManyField(Distributer)
    category = models.CharField(max_length=250, choices=CATEGORIES)

    @property
    def added_on(self):
        return timesince(self.created) + " ago"

    def __str__(self):
        return self.name + " - " + str(self.id)

    def save(self):
        self.slug = slugify(self.name)
        return super().save()

    class Meta:
        # abstract = True
        db_table = 'product'
        ordering = ['-price', 'created']


def pre_save_product_receiver(sender, instance, *args, **kwargs):
    print("PRE SAVE")
    if not instance.name.endswith(' - Hi'):
        instance.name = instance.name + " - Hi"
    # return instance.save()


pre_save.connect(pre_save_product_receiver, sender=Product)


def post_save_product_receiver(sender, instance, created, *args, **kwargs):
    print("POST SAVE")
    if created:
        tax = instance.price * 0.1
        instance.price = instance.price + tax
        return instance.save()


post_save.connect(post_save_product_receiver, sender=Product)
