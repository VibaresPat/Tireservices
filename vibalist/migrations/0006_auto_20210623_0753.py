# Generated by Django 3.1.6 on 2021-06-23 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vibalist', '0005_auto_20210623_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantdetails',
            name='grad',
            field=models.CharField(choices=[('selectmethodS', 'BANK ACCOUNT'), ('slctmthdS', 'GCASH'), ('slectmthodS', 'CREDIT CARD')], default='none', max_length=25),
        ),
    ]