# Generated by Django 4.0.5 on 2022-06-28 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='contact',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
