# Generated by Django 3.1.4 on 2021-01-07 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('consultation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultation',
            name='blood_pressure',
        ),
        migrations.AddField(
            model_name='consultation',
            name='blood_pressure_a',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='consultation',
            name='blood_pressure_b',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='admit',
            name='specialist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
