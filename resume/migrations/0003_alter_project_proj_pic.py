# Generated by Django 3.2.7 on 2021-09-30 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_remove_project_personal_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='proj_pic',
            field=models.ImageField(blank=True, upload_to='my_project_pics/'),
        ),
    ]
