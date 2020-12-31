# Generated by Django 3.1.4 on 2020-12-16 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201216_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.IntegerField(choices=[(0, 'Female'), (1, 'Male'), (2, 'Lesbian'), (3, 'Gay'), (4, 'Bisexual'), (5, 'Transgender'), (6, 'Queer')], default=0),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.IntegerField(choices=[(0, 'Doctor'), (1, 'Pharmacist'), (2, 'Patient')], default=0),
        ),
    ]