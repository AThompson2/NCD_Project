# Generated by Django 2.2.1 on 2019-12-28 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0011_auto_20191228_1151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Ivoice_pdf',
            new_name='Invoice_pdf',
        ),
    ]
