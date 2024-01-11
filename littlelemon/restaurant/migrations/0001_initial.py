# Generated by Django 5.0.1 on 2024-01-11 16:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(limit_value=99999999999)])),
                ('name', models.CharField(max_length=255)),
                ('no_of_guests', models.IntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=6)])),
                ('reservation_slot', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(limit_value=99999999999)])),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('inventory', models.IntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=99999)])),
            ],
        ),
    ]
