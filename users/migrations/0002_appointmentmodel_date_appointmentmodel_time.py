# Generated by Django 4.2.11 on 2024-05-01 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentmodel',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='appointmentmodel',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
