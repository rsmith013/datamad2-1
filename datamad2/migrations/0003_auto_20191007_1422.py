# Generated by Django 2.2.6 on 2019-10-07 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datamad2', '0002_auto_20191007_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grant',
            name='grant_ref',
        ),
        migrations.RemoveField(
            model_name='grant',
            name='title',
        ),
    ]
