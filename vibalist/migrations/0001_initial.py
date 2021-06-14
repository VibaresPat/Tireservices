# Generated by Django 3.1.6 on 2021-06-13 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grad', models.CharField(choices=[('selectmethod', 'BANK ACCOUNT'), ('slctmthd', 'GCASH'), ('slectmthod', 'CREDIT CARD')], default='none', max_length=25)),
                ('schools', models.CharField(default='none', max_length=10)),
                ('maj', models.CharField(default='none', max_length=10)),
                ('deg', models.CharField(default='none', max_length=10)),
                ('taon', models.CharField(default='none', max_length=10)),
                ('schl', models.CharField(default='none', max_length=10)),
                ('jor', models.CharField(default='none', max_length=10)),
                ('ree', models.CharField(default='none', max_length=10)),
                ('yea', models.CharField(default='none', max_length=10)),
                ('award', models.CharField(default='none', max_length=10)),
                ('avail', models.CharField(default='none', max_length=10)),
                ('hayts', models.CharField(default='none', max_length=10)),
                ('oras', models.CharField(default='none', max_length=10)),
                ('teach', models.CharField(default='none', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicantInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant', models.CharField(default='none', max_length=10)),
                ('last', models.CharField(default='none', max_length=10)),
                ('email', models.CharField(default='none', max_length=10)),
                ('cell', models.CharField(default='none', max_length=10)),
                ('ress', models.CharField(default='none', max_length=10)),
                ('zipss', models.CharField(default='none', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicantTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='none', max_length=10)),
                ('Transfering', models.CharField(choices=[('salary', 'Gcash'), ('slry', 'Bank Account'), ('sltss', 'Credit Card')], default='none', max_length=25)),
                ('gcashh', models.CharField(default='none', max_length=10)),
                ('hold', models.CharField(default='none', max_length=10)),
                ('carddy', models.CharField(default='none', max_length=10)),
                ('bankyy', models.CharField(default='none', max_length=10)),
                ('acc', models.CharField(default='none', max_length=10)),
                ('nice', models.CharField(default='none', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ClientInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Childname', models.CharField(default='none', max_length=10)),
                ('Guardianname', models.CharField(default='none', max_length=10)),
                ('Age', models.CharField(default='none', max_length=10)),
                ('Cellphone', models.CharField(default='none', max_length=10)),
                ('Location', models.CharField(default='none', max_length=10)),
                ('mail', models.CharField(default='none', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField(null=True)),
                ('TOTAL', models.IntegerField(null=True)),
                ('Quantity1', models.IntegerField(null=True)),
                ('TOTAL2', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paymentmethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selectsss', models.CharField(choices=[('selectmethod', 'BANK ACCOUNT'), ('slctmthd', 'GCASH'), ('slectmthod', 'CREDIT CARD')], default='none', max_length=25)),
                ('Holder', models.CharField(default='none', max_length=10)),
                ('Bank', models.CharField(default='none', max_length=10)),
                ('Account', models.CharField(default='none', max_length=10)),
                ('Routing', models.CharField(default='none', max_length=10)),
                ('payment', models.CharField(default='none', max_length=10)),
                ('Amount', models.CharField(default='none', max_length=10)),
                ('card', models.CharField(default='none', max_length=10)),
                ('Expiry', models.CharField(default='none', max_length=10)),
                ('code', models.CharField(default='none', max_length=10)),
                ('zips', models.CharField(default='none', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Scheduling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(null=True)),
                ('Subject1', models.CharField(default='none', max_length=10)),
                ('Schedule', models.CharField(default='none', max_length=10)),
                ('Time', models.TimeField(null=True)),
                ('Message', models.TextField(default='none', max_length=2000)),
                ('sltss', models.CharField(choices=[('selecthome', 'Home Visiting'), ('selectonline', 'Online'), ('selecthouse', 'Teacher House')], default='none', max_length=25)),
                ('place', models.CharField(choices=[('min', 'Mindanao'), ('vis', 'Visayas'), ('luz', 'Luzon'), ('metro', 'Metro Manila')], default='none', max_length=25)),
                ('Transportation_Amount', models.CharField(default='none', max_length=10)),
            ],
        ),
    ]
