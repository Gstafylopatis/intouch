# Generated by Django 3.2.8 on 2021-10-30 17:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_order_orderitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='purchace_price',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=7, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.DecimalField(decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]