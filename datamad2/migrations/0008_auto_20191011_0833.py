# Generated by Django 2.2.6 on 2019-10-11 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamad2', '0007_auto_20191011_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importedgrant',
            name='claim_status',
            field=models.CharField(blank=True, choices=[('Claimed', 'Claimed')], max_length=200, null=True),
        ),
    ]
