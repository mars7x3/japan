# Generated by Django 4.0.5 on 2022-08-23 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('star', '0005_remove_starordervideo_user_remove_starprofile_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.CharField(default=1, max_length=100, verbose_name='Пользователь'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='StarQuestionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager', models.CharField(max_length=100, verbose_name='Менеджер звезды')),
                ('phone', models.CharField(max_length=50, verbose_name='Номер менеджера')),
                ('price', models.CharField(max_length=50, verbose_name='Цена за выступление')),
                ('location', models.CharField(max_length=200, verbose_name='Город')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionnaire', to='star.starprofile', verbose_name='Звезда')),
            ],
        ),
    ]
