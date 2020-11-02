# Generated by Django 2.2.5 on 2020-10-29 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20201026_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('confimed', 'Confirmed'), ('canceled', 'Canceled')], default='pending', max_length=12),
        ),
    ]