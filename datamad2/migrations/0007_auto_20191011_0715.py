# Generated by Django 2.2.6 on 2019-10-11 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamad2', '0006_importedgrant_claim_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importedgrant',
            name='claim_status',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]