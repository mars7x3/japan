# Generated by Django 4.0.5 on 2022-08-23 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('star', '0004_alter_starprofile_star_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='starordervideo',
            name='user',
        ),
        migrations.RemoveField(
            model_name='starprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='starprofile',
            name='video',
        ),
        migrations.RemoveField(
            model_name='starreview',
            name='user',
        ),
        migrations.AddField(
            model_name='starordervideo',
            name='star',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='star_video', to='star.starprofile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='star',
            field=models.CharField(max_length=200, verbose_name='Звезда'),
        ),
        migrations.RemoveField(
            model_name='starprofile',
            name='category',
        ),
        migrations.AddField(
            model_name='starprofile',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='star_profile', to='star.starcategory'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='starprofile',
            name='deadline',
            field=models.IntegerField(default=3, verbose_name='Срок выполнения'),
        ),
    ]