# Generated by Django 2.2.9 on 2020-06-22 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0005_auto_20200622_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='kategorien',
            name='title_2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]