# Generated by Django 4.2.7 on 2023-11-17 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='analytic',
            name='device_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
