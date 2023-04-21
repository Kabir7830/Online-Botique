# Generated by Django 4.1 on 2023-04-18 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0005_rename_photo_clothes_photo1_clothes_photo2_and_more'),
        ('customers', '0005_delete_customer_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customers')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clothes.clothes')),
            ],
            options={
                'db_table': 'Customer_Cart',
            },
        ),
    ]
