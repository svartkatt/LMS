# Generated by Django 3.1.6 on 2021-03-17 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='covers',
            field=models.ImageField(default='covers/default.png', upload_to='covers/'),
        ),
    ]
