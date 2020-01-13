# Generated by Django 2.2.1 on 2019-12-03 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_auto_20191201_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Products.ProductDB'),
        ),
    ]
