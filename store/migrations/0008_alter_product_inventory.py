# Generated by Django 3.2.8 on 2021-10-30 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_rename_purchace_price_product_purchase_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='inventory',
            field=models.DecimalField(decimal_places=1, max_digits=7),
        ),
    ]
