# Generated by Django 4.1.7 on 2023-02-28 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_latitud_project_name_talk'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Talk',
            new_name='Task',
        ),
    ]