# Generated by Django 4.1.2 on 2023-01-22 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Notes",
            new_name="Note",
        ),
    ]