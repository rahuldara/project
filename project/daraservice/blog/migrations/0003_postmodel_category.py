# Generated by Django 4.2.1 on 2023-06-30 12:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_postmodel_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='category',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
