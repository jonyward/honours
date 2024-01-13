# Generated by Django 4.2.8 on 2024-01-08 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crash_vis', '0003_crash_delete_crashes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crashes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Longitude', models.FloatField(verbose_name='Longitude')),
                ('Latitude', models.FloatField(verbose_name='Longitude')),
            ],
        ),
        migrations.DeleteModel(
            name='Crash',
        ),
    ]