# Generated by Django 4.1.4 on 2022-12-14 17:58

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('available', django.db.models.manager.Manager()),
            ],
        ),
    ]
