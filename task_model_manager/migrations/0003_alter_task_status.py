# Generated by Django 4.0.3 on 2022-07-07 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_model_manager', '0002_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]