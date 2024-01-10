# Generated by Django 3.0.6 on 2024-01-01 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metapp', '0009_auto_20231230_0316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('student', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('invoice', models.FileField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Reciepts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('student', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('reciept', models.FileField(upload_to='media')),
            ],
        ),
    ]