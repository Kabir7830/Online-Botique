# Generated by Django 4.1 on 2023-04-18 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0009_subscribe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='joining_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]