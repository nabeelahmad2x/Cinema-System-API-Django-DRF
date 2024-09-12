# Generated by Django 5.1.1 on 2024-09-12 09:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cinemahalls', '0001_initial'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shows',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('show_date', models.DateField()),
                ('timeslot', models.CharField()),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('show_status', models.CharField()),
                ('cinema_hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemahalls.cinemahall')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
            options={
                'unique_together': {('cinema_hall', 'show_date', 'timeslot')},
            },
        ),
    ]
