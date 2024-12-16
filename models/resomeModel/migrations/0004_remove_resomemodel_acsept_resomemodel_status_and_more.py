# Generated by Django 5.0 on 2024-11-23 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resomeModel', '0003_alter_resomemodel_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resomemodel',
            name='acsept',
        ),
        migrations.AddField(
            model_name='resomemodel',
            name='status',
            field=models.IntegerField(choices=[(0, 'قبول نشده'), (1, 'قبول شده'), (2, 'دیده نشده'), (3, 'دیده شده')], default=0, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='resomemodel',
            name='show',
            field=models.IntegerField(choices=[(0, 'تایید'), (1, 'رد')], default=0, verbose_name='وضغیت مشاهده'),
        ),
    ]