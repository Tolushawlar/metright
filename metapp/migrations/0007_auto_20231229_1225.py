# Generated by Django 3.0.6 on 2023-12-29 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metapp', '0006_auto_20231227_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('staff', models.TextField()),
                ('student', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('assignment', models.FileField(upload_to='media')),
            ],
        ),
        migrations.AddField(
            model_name='reports',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]