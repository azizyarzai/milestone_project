# Generated by Django 3.2.9 on 2021-12-02 03:45

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='test', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(error_messages={'blank': 'please enter the name', 'unique': 'the value is not unique'}, max_length=20, validators=[products.models.check_for_phone]),
        ),
    ]
