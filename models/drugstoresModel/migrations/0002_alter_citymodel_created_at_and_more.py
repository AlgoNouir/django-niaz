# Generated by Django 5.0 on 2024-11-23 09:29

import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drugstoresModel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citymodel',
            name='created_at',
            field=django_jalali.db.models.jDateField(auto_now=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='drugstoresmodel',
            name='created_at',
            field=django_jalali.db.models.jDateField(auto_now=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='personmodel',
            name='created_at',
            field=django_jalali.db.models.jDateField(auto_now=True, verbose_name='تاریخ ایجاد'),
        ),
    ]
