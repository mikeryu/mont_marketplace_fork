# Generated by Django 5.0.1 on 2024-02-25 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_remove_listing_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='photo',
            field=models.ImageField(blank=True, default='static/listings/default_image.jpeg', null=True, upload_to='listings'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='seller',
            field=models.IntegerField(default=1),
        ),
    ]
