# Generated by Django 5.0 on 2024-11-23 12:06

import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_karfarmamodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='karfarmamodel',
            name='date',
            field=django_jalali.db.models.jDateField(null=True, verbose_name='تاریخ تاسیس'),
        ),
    ]