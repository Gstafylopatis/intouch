# Generated by Django 3.2.8 on 2021-10-30 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20211030_2002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='purchace_price',
            new_name='purchase_price',
        ),
    ]
