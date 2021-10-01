# Generated by Django 3.2.7 on 2021-10-01 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('topic', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('proj_pic', models.ImageField(upload_to='my_project_pics/')),
                ('proj_url', models.URLField()),
                ('client', models.CharField(blank=True, max_length=100)),
                ('project_created', models.DateTimeField()),
            ],
            options={
                'ordering': ('project_created',),
            },
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField(default=0)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('profile_pic', models.ImageField(upload_to='my_pics/')),
                ('about_me', models.TextField(blank=True)),
                ('skills', models.CharField(max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('personal_detail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Acomplishment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_completed', models.IntegerField(default=0, help_text='Total Work Completed')),
                ('years_of_exper', models.IntegerField(default=0, help_text='Years of Experience.')),
                ('total_client', models.IntegerField(default=0, help_text='Total Client Worked For.')),
                ('award_won', models.IntegerField(default=0, help_text='Award Won.')),
                ('personal_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acomplishment', to='resume.detail')),
            ],
        ),
    ]
