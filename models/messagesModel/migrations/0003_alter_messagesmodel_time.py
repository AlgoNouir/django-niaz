# Generated by Django 5.0 on 2024-11-23 09:31

import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messagesModel', '0002_alter_messagesmodel_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagesmodel',
            name='time',
            field=django_jalali.db.models.jDateField(verbose_name='زمان'),
        ),
    ]