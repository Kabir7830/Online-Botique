# Generated by Django 4.1.7 on 2023-03-01 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=20)),
                ('material', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Clothes',
            },
        ),
    ]
