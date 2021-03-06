# Generated by Django 3.2.7 on 2022-05-08 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_alter_detail_backgroud_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_owner', to='resume.detail'),
        ),
        migrations.AlterField(
            model_name='acomplishment',
            name='award_won',
            field=models.PositiveIntegerField(default=0, help_text='Award Won.'),
        ),
        migrations.AlterField(
            model_name='acomplishment',
            name='total_client',
            field=models.PositiveIntegerField(default=0, help_text='Total Client Worked For.'),
        ),
        migrations.AlterField(
            model_name='acomplishment',
            name='work_completed',
            field=models.PositiveIntegerField(default=0, help_text='Total Work Completed'),
        ),
        migrations.AlterField(
            model_name='acomplishment',
            name='years_of_exper',
            field=models.PositiveIntegerField(default=0, help_text='Years of Experience.'),
        ),
    ]
