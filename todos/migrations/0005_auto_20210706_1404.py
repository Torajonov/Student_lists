# Generated by Django 3.2.4 on 2021-07-06 09:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0004_auto_20190408_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='adress',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='Manzili'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='phone',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='Telefon raqami'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='surname',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='familiyasi'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='item',
            field=models.CharField(max_length=200, verbose_name='ismi'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
