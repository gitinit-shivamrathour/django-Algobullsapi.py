# Generated by Django 4.2.1 on 2023-06-01 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(default='OPEN', max_length=100),
        ),
    ]
