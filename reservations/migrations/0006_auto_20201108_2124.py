# Generated by Django 2.2.5 on 2020-11-08 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0005_auto_20201108_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('canceled', 'Canceled'), ('confimed', 'Confirmed')], default='pending', max_length=12),
        ),
    ]
