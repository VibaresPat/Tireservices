# Generated by Django 3.1.6 on 2021-06-23 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vibalist', '0010_auto_20210623_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicanttransfer',
            name='Transfering',
            field=models.CharField(choices=[('1', 'Gcash'), ('2', 'Bank Account'), ('3', 'Credit Card')], default='none', max_length=25),
        ),
    ]
