# Generated by Django 2.2 on 2019-07-06 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='term',
            field=models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='activate', max_length=10),
        ),
    ]