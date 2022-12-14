# Generated by Django 4.0.5 on 2022-08-27 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('star', '0014_starcategory_category_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToastsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Toasts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Текст')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='star.toastscategory', verbose_name='Категория')),
            ],
        ),
    ]
