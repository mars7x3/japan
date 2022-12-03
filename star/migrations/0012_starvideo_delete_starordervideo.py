# Generated by Django 4.0.5 on 2022-08-23 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('star', '0011_managerorder_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='StarVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='star-video-image', verbose_name='Обложка видео')),
                ('video', models.FileField(upload_to='star-order-video', verbose_name='Видео')),
                ('banner', models.ImageField(upload_to='star-banner-image', verbose_name='Баннер')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='star_video', to='star.starprofile')),
            ],
        ),
        migrations.DeleteModel(
            name='StarOrderVideo',
        ),
    ]