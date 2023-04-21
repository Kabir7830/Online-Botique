# Generated by Django 4.1 on 2023-04-11 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0004_clothes_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clothes',
            old_name='photo',
            new_name='photo1',
        ),
        migrations.AddField(
            model_name='clothes',
            name='photo2',
            field=models.FileField(blank=True, null=True, upload_to='cloth_pics'),
        ),
        migrations.AddField(
            model_name='clothes',
            name='photo3',
            field=models.FileField(blank=True, null=True, upload_to='cloth_pics'),
        ),
        migrations.AddField(
            model_name='clothes',
            name='photo4',
            field=models.FileField(blank=True, null=True, upload_to='cloth_pics'),
        ),
        migrations.AddField(
            model_name='clothes',
            name='photo5',
            field=models.FileField(blank=True, null=True, upload_to='cloth_pics'),
        ),
        migrations.AddField(
            model_name='clothes',
            name='photo6',
            field=models.FileField(blank=True, null=True, upload_to='cloth_pics'),
        ),
    ]