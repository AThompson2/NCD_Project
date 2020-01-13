# Generated by Django 2.2.1 on 2019-12-01 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_auto_20190906_1604'),
        ('checkout', '0005_remove_cartitem_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='price',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Products.ProductDB'),
        ),
    ]