# Generated by Django 5.0 on 2024-11-23 09:29

import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storesModel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storesmodel',
            name='created_at',
            field=django_jalali.db.models.jDateField(auto_now=True, verbose_name='تاریخ ایجاد'),
        ),
    ]