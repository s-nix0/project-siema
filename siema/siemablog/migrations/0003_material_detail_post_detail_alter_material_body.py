# Generated by Django 4.2.7 on 2023-11-03 02:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('siemablog', '0002_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='detail',
            field=models.TextField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='detail',
            field=models.TextField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='material',
            name='body',
            field=models.TextField(),
        ),
    ]
