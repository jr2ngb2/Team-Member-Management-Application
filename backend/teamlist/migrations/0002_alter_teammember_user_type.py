# Generated by Django 4.0 on 2021-12-19 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='user_type',
            field=models.CharField(blank=True, choices=[('USER_REGULAR', 'REGULAR'), ('USER_ADMIN', 'ADMIN')], default='USER_REGULAR', max_length=20),
        ),
    ]
