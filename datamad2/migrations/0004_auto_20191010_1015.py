# Generated by Django 2.2.6 on 2019-10-10 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamad2', '0003_auto_20191007_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importedgrant',
            name='science_area',
            field=models.CharField(blank=True, choices=[('Marine', 'Marine'), ('Earth', 'Earth'), ('Atmospheric', 'Atmospheric'), ('Freshwater', 'Freshwater'), ('Terrestrial', 'Terrestrial')], max_length=200, null=True),
        ),
    ]
