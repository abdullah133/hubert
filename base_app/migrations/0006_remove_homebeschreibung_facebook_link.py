# Generated by Django 3.0.7 on 2020-06-09 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0005_auto_20200609_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homebeschreibung',
            name='facebook_link',
        ),
    ]
