# Generated by Django 3.1.6 on 2021-03-17 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0003_student_covers'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='covers',
            field=models.ImageField(default='covers/default.png', upload_to='covers/'),
        ),
    ]
