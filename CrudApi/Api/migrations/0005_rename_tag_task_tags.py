# Generated by Django 4.2.1 on 2023-06-01 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0004_rename_tags_task_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='tag',
            new_name='tags',
        ),
    ]
