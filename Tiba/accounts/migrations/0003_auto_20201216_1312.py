# Generated by Django 3.1.4 on 2020-12-16 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201216_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.IntegerField(choices=[(0, 'Doctor'), (1, 'Pharmacist'), (2, 'Patient')]),
        ),
    ]
