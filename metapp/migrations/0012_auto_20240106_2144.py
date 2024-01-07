# Generated by Django 3.0.6 on 2024-01-06 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metapp', '0011_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course2_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondary_course_students', to='metapp.Course'),
        ),
        migrations.AddField(
            model_name='student',
            name='course3_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tertiary_course_students', to='metapp.Course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_course_students', to='metapp.Course'),
        ),
    ]
