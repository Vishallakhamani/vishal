# Generated by Django 4.0.5 on 2022-06-25 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0002_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('remarks', models.TextField()),
            ],
        ),
    ]
