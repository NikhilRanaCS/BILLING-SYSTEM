# Generated by Django 4.2.11 on 2024-04-07 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_products_bill_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='product',
            new_name='products',
        ),
    ]
