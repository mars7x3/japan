# Generated by Django 4.0.5 on 2022-08-23 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('star', '0003_starprofile_popular_starprofile_star_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='starprofile',
            name='star_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID популярные'),
        ),
    ]
