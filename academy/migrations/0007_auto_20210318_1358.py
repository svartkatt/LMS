# Generated by Django 3.1.6 on 2021-03-18 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0006_auto_20210318_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecturer',
            old_name='cover',
            new_name='avatar',
        ),
    ]
