# Generated by Django 2.2.1 on 2020-06-13 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metapp', '0004_auto_20200612_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavereportstudent',
            name='leave_status',
            field=models.IntegerField(default=0),
        ),
    ]