# Generated by Django 2.2.1 on 2019-12-28 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0013_auto_20191228_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Invoice_pdf',
            field=models.FileField(blank=True, null=True, upload_to='static'),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(default='', max_length=191),
        ),
    ]