# Generated by Django 3.2.9 on 2021-11-27 03:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='update',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]