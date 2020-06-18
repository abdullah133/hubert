# Generated by Django 3.0.7 on 2020-06-08 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0002_remove_kontaktinfo_adresse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kontaktinfo',
            name='iban',
        ),
        migrations.RemoveField(
            model_name='kontaktinfo',
            name='instagram_link',
        ),
        migrations.RemoveField(
            model_name='kontaktinfo',
            name='twitter_link',
        ),
        migrations.RemoveField(
            model_name='kontaktinfo',
            name='zvr_zahl',
        ),
        migrations.AlterField(
            model_name='kontaktinfo',
            name='email',
            field=models.CharField(max_length=300, verbose_name='E-Mail Adresse'),
        ),
        migrations.AlterField(
            model_name='kontaktinfo',
            name='name',
            field=models.CharField(default='Hubert Mayr', max_length=300, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='kontaktinfo',
            name='telefon',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Telefon Nr.'),
        ),
    ]
