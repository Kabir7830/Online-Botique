# Generated by Django 4.1 on 2023-04-18 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_customer_cart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer_Cart',
        ),
    ]