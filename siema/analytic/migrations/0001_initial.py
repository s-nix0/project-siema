# Generated by Django 4.2.7 on 2023-11-17 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analytic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_url', models.CharField(blank=True, max_length=255, null=True)),
                ('view_count', models.IntegerField(default=0)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user_agent', models.CharField(blank=True, max_length=255, null=True)),
                ('referrer', models.URLField(blank=True, null=True)),
                ('error_message', models.TextField(blank=True, null=True)),
                ('request_method', models.CharField(blank=True, max_length=10, null=True)),
                ('status_code', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
