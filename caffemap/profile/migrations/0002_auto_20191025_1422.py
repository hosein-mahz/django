# Generated by Django 2.2 on 2019-10-25 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ('name',)},
        ),
    ]