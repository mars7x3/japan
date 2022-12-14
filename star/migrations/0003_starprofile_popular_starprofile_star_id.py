# Generated by Django 4.0.5 on 2022-08-23 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('star', '0002_alter_starcategory_options_alter_starprofile_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='starprofile',
            name='popular',
            field=models.BooleanField(default=False, verbose_name='Категория популярные'),
        ),
        migrations.AddField(
            model_name='starprofile',
            name='star_id',
            field=models.CharField(default=1, max_length=50, verbose_name='ID популярные'),
            preserve_default=False,
        ),
    ]
