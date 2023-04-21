# Generated by Django 4.1 on 2023-03-31 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0002_clothes_name_clothes_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes_Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Clothes_Categories',
            },
        ),
        migrations.AddField(
            model_name='clothes',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='clothes.clothes_categories'),
            preserve_default=False,
        ),
    ]
