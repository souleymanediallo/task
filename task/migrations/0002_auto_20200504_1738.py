# Generated by Django 3.0.6 on 2020-05-04 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='context',
            new_name='content',
        ),
    ]