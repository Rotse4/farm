# Generated by Django 5.0.3 on 2024-04-01 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FarmHoldings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('acrage', models.IntegerField()),
                ('areaunit', models.CharField(max_length=50)),
                ('landsize', models.IntegerField()),
                ('lat', models.DecimalField(decimal_places=5, max_digits=10, null=True)),
                ('long', models.DecimalField(decimal_places=5, max_digits=10, null=True)),
                ('accuracy', models.IntegerField()),
                ('legstatus', models.CharField(max_length=100)),
                ('other_farms', models.BooleanField()),
            ],
        ),
    ]
