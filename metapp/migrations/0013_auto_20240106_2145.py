# Generated by Django 3.0.6 on 2024-01-06 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metapp', '0012_auto_20240106_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='staff2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='staff3',
            field=models.TextField(blank=True, null=True),
        ),
    ]
