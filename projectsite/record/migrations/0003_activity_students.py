# Generated by Django 5.0 on 2023-12-29 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_activity_score_assignment_score_exam_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='students',
            field=models.ManyToManyField(related_name='activities', to='record.student'),
        ),
    ]
