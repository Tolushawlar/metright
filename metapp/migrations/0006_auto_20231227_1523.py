# Generated by Django 3.0.6 on 2023-12-27 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metapp', '0005_reports'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='report',
            field=models.FileField(upload_to='media'),
        ),
    ]
