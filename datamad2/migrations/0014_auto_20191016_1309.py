# Generated by Django 2.2.6 on 2019-10-16 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamad2', '0013_auto_20191016_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='data_centre',
            field=models.CharField(blank=True, choices=[('Unassigned', 'Unassigned'), ('BODC', 'BODC'), ('CEDA', 'CEDA'), ('EIDC', 'EIDC'), ('NGDC', 'NGDC'), ('PDC', 'PDC'), ('ADS', 'ADS')], max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='DataCentre',
        ),
    ]