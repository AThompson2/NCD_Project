# Generated by Django 2.2.1 on 2020-01-12 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0009_auto_20191208_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdb',
            name='product_pic',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
