# Generated by Django 3.2.7 on 2022-05-08 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_remove_acomplishment_personal_detail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='backgroud_pic',
            new_name='_backgroud_pic',
        ),
        migrations.RenameField(
            model_name='detail',
            old_name='profile_pic',
            new_name='_profile_pic',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='proj_pic',
            new_name='_proj_pic',
        ),
    ]