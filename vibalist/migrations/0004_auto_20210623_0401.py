# Generated by Django 3.1.6 on 2021-06-23 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vibalist', '0003_auto_20210623_0351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scheduling',
            old_name='Transportation_Amount',
            new_name='TransportationAmount',
        ),
    ]