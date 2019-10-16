# Generated by Django 2.2.6 on 2019-10-11 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamad2', '0010_auto_20191011_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='assigned_data_centre',
            field=models.CharField(blank=True, choices=[('Unassigned', 'Unassigned'), ('BODC', 'BODC'), ('CEDA', 'CEDA'), ('EIDC', 'EIDC'), ('NGDC', 'NGDC'), ('PDC', 'PDC'), ('ADS', 'ADS')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='grant',
            name='other_data_centre',
            field=models.CharField(blank=True, choices=[('None', 'None'), ('BODC', 'BODC'), ('CEDA', 'CEDA'), ('EIDC', 'EIDC'), ('NGDC', 'NGDC'), ('PDC', 'PDC'), ('ADS', 'ADS')], max_length=200, null=True),
        ),
    ]