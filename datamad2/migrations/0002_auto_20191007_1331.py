# Generated by Django 2.2.6 on 2019-10-07 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamad2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grant',
            name='grant_ref',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='grant',
            name='title',
            field=models.CharField(default='', max_length=1024),
        ),
    ]
