# Generated by Django 5.0 on 2024-11-19 16:14

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='KarfarmamodelProxy',
            fields=[
            ],
            options={
                'verbose_name': 'کارفرما',
                'verbose_name_plural': 'کارفرما ها',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('user.allusers',),
        ),
    ]