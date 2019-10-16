# Generated by Django 2.2.6 on 2019-10-11 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamad2', '0004_auto_20191010_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importedgrant',
            name='routing_classification',
            field=models.CharField(blank=True, choices=[('Marine', 'Marine'), ('Earth', 'Earth'), ('Atmospheric', 'Atmospheric'), ('Freshwater', 'Freshwater'), ('Terrestrial', 'Terrestrial')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='importedgrant',
            name='science_area',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]