# Generated by Django 3.1.6 on 2021-06-23 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vibalist', '0007_auto_20210623_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmethod',
            name='selectsss',
            field=models.CharField(choices=[('1', 'BANK ACCOUNT'), ('2', 'GCASH'), ('3', 'CREDIT CARD')], default='none', max_length=25),
        ),
    ]