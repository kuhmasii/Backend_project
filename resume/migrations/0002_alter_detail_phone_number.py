# Generated by Django 3.2.7 on 2021-10-06 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='phone_number',
            field=models.CharField(blank=True, max_length=16),
        ),
    ]
