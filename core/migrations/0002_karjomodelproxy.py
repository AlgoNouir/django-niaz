# Generated by Django 5.0 on 2024-11-23 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('user', '0002_alter_allusers_created_at_alter_allusers_username_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='KarjomodelProxy',
            fields=[
            ],
            options={
                'verbose_name': 'کارجو',
                'verbose_name_plural': 'کارجو ها',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('user.allusers',),
        ),
    ]
