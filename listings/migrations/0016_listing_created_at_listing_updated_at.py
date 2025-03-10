# Generated by Django 5.0.1 on 2024-02-28 22:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0015_alter_montuser_email_alter_montuser_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
