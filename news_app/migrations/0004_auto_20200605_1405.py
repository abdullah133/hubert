# Generated by Django 3.0.7 on 2020-06-05 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0003_auto_20200605_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='News/pdf/'),
        ),
    ]