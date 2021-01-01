# Generated by Django 3.1.4 on 2021-01-01 17:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consultation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drugs',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('medicine_type', models.CharField(max_length=240)),
                ('unit', models.IntegerField(default=0)),
                ('unit_remaining', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('consultation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultation.consultation')),
                ('drug_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drugs.drugs')),
            ],
        ),
    ]