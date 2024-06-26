# Generated by Django 5.0.3 on 2024-03-31 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnumarationGeography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(max_length=100)),
                ('constituency', models.CharField(max_length=100)),
                ('sub_county', models.CharField(max_length=100)),
                ('ward', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('sub_location', models.CharField(max_length=100)),
                ('village_unit_name', models.CharField(max_length=100)),
                ('enumaration_area_no', models.CharField(max_length=100)),
                ('shopping_center', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='IndividualDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_name', models.CharField(max_length=100)),
                ('national_id', models.BigIntegerField()),
                ('email', models.CharField(max_length=100)),
                ('year_of_birth', models.DateTimeField()),
                ('postal', models.CharField(max_length=100)),
                ('postal_code', models.IntegerField()),
                ('mobile_number', models.CharField(max_length=100)),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Maried', 'Maried')], default='Single', max_length=100)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('hh_size', models.IntegerField()),
                ('training', models.BooleanField()),
            ],
        ),
    ]
