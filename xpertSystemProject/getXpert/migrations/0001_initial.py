# Generated by Django 2.1.2 on 2018-11-29 04:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_active', models.BooleanField(db_column='is_active', default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.CharField(blank=True, max_length=256, null=True)),
                ('date_of_birth', models.CharField(blank=True, max_length=10)),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('permanent_address', models.CharField(max_length=300)),
                ('qualification', models.CharField(blank=True, max_length=120)),
                ('occupation', models.CharField(blank=True, max_length=120)),
                ('skills', models.TextField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('Available_service_area', models.CharField(blank=True, max_length=120)),
                ('languages_spoken', models.CharField(blank=True, max_length=120)),
                ('Working_experience', models.CharField(blank=True, max_length=120)),
                ('charges', models.CharField(blank=True, max_length=5)),
                ('Profile_Tagline', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='getXpert.User')),
            ],
        ),
    ]
