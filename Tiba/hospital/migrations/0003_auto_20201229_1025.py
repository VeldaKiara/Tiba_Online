# Generated by Django 3.1.4 on 2020-12-29 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_auto_20201229_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='hospital_level',
            field=models.CharField(choices=[('1', 'Community Facilities, Level 1'), ('2', 'Health Dispensaries, Level 2'), ('3', 'Health Centres, Level 3'), ('4', 'County Hospitals, Level 4'), ('5', 'County Referral Hospitals, Level 5'), ('6', 'National Referral Hospitals, Level 6')], default=1, max_length=250),
        ),
    ]
