# Generated by Django 4.1.6 on 2023-02-04 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='file_1',
            field=models.FileField(null=True, upload_to='article/files/'),
        ),
        migrations.AddField(
            model_name='article',
            name='file_2',
            field=models.FileField(null=True, upload_to='article/files/'),
        ),
        migrations.AddField(
            model_name='article',
            name='file_3',
            field=models.FileField(null=True, upload_to='article/files/'),
        ),
    ]
