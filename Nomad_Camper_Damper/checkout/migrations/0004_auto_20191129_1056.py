# Generated by Django 2.2.1 on 2019-11-28 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_auto_20190906_1604'),
        ('checkout', '0003_auto_20191128_0638'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Products.ProductDB'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='price',
            field=models.IntegerField(),
        ),
    ]
