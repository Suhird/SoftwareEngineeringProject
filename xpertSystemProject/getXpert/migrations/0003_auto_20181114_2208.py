# Generated by Django 2.1.2 on 2018-11-15 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getXpert', '0002_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(db_column='is_active', default=False),
        ),
    ]