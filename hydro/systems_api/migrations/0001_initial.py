# Generated by Django 5.0.6 on 2024-06-02 15:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HydroponicSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hydroponic_systems', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HydroponicSystemMeasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pH', models.DecimalField(decimal_places=2, max_digits=4)),
                ('temperature', models.FloatField()),
                ('TDS', models.FloatField()),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='systems_api.hydroponicsystem')),
            ],
        ),
    ]
