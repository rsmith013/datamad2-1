# Generated by Django 2.2.6 on 2019-11-18 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datamad2', '0026_auto_20191118_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='importedgrant',
            name='parent_grant',
        ),
    ]
