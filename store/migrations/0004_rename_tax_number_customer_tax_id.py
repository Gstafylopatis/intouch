# Generated by Django 3.2.8 on 2021-10-27 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_customer_tax_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='tax_number',
            new_name='tax_id',
        ),
    ]